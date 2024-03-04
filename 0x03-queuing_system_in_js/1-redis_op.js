import { createClient, print } from 'redis';

const client = createClient();

function redisConnection() {
    client.on('connect', () => {
        console.log('Redis client connected to the server');
    });

    client.on('error', (err) => {
        console.error(`Redis client not connected to the server: ${err}`);
    });
}

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
