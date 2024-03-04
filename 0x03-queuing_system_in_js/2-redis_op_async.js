import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

function redisConnection() {
    client.on('connect', () => {
        console.log('Redis client connected to the server');
    });

    client.on('error', (err) => {
        console.error(`Redis client not connected to the server: ${err}`);
    });
}

const get = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, function (error, result) {
        if (error) {
            console.log(error);
            throw error;
        }
        console.log(result);
    });
}


redisConnection();

displaySchoolValue('Holberton');

setNewSchool('HolbertonSanFrancisco', '100');

displaySchoolValue('HolbertonSanFrancisco');
