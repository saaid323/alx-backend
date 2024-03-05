import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));

client.on('error', err => console.log('Redis client not connected to the server:', err.toString()));

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, client.print);
}

function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, res) => {
		console.log(res);
	});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
