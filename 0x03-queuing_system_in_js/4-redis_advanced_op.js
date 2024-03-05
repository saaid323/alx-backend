import { createClient } from 'redis';
const util = require('util')
const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));

client.on('error', err => console.log('Redis client not connected to the server:', err.toString()));

client.hset('HolbertonSchools', 'Portland', 50, client.print);
client.hset('HolbertonSchools', 'Seattle', 80, client.print);
client.hset('HolbertonSchools', 'New York', 20, client.print);
client.hset('HolbertonSchools', 'Bogota', 20, client.print);
client.hset('HolbertonSchools', 'Cali', 40, client.print);
client.hset('HolbertonSchools', 'Paris', 2, client.print);

client.hgetall('HolbertonSchools', (err, obj) => {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log(obj);
  }
});
