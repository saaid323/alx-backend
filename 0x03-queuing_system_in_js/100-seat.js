const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

const queue = kue.createQueue();
const app = express();
const port = 1245;
const initialSeats = 50;
let reservationEnabled = true;
let availableSeats = initialSeats;

async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return parseInt(seats);
}

function checkReservation(req, res, next) {
    if (!reservationEnabled) {
        res.json({ "status": "Reservation are blocked" });
    } else {
        next();
    }
}

app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats();
    res.json({ "numberOfAvailableSeats": seats });
});

app.get('/reserve_seat', checkReservation, (req, res) => {
    const job = queue.create('reserve_seat').save((err) => {
        if (err) {
            res.json({ "status": "Reservation failed" });
        } else {
            res.json({ "status": "Reservation in process" });
        }
    });
});

app.get('/process', async (req, res) => {
    res.json({ "status": "Queue processing" });

    queue.process('reserve_seat', async (job, done) => {
        try {
            const currentSeats = await getCurrentAvailableSeats();
            if (currentSeats === 0) {
                reservationEnabled = false;
            } else if (currentSeats < 0) {
                throw new Error('Not enough seats available');
            } else {
                await reserveSeat(currentSeats - 1);
            }
            console.log(`Seat reservation job ${job.id} completed`);
            done();
        } catch (error) {
            console.log(`Seat reservation job ${job.id} failed: ${error.message}`);
            done(error);
        }
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

reserveSeat(initialSeats)
    .then(() => console.log('Available seats initialized in Redis'))
    .catch(error => console.error('Error initializing available seats in Redis:', error));

