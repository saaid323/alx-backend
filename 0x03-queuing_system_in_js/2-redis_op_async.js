import { createClient } from 'redis';
const util = require('util')
const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));

client.on('error', err => console.log('Redis client not connected to the server:', err.toString()));

function setNewSchool(schoolName, value) {
        client.set(schoolName, value, client.print);
}

const getAsync = util.promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
	const value = await getAsync(schoolName);
	console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
