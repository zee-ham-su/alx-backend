import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const get = promisify(client.get).bind(client);

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

async function displaySchoolValue(schoolName) {
    const output = await get(schoolName).catch((err) =>{
        if (error) {
            console.log(error);
            throw error;
        }
    });
        console.log(output);
    }


redisConnection();

displaySchoolValue('Holberton');

setNewSchool('HolbertonSanFrancisco', '100');

displaySchoolValue('HolbertonSanFrancisco');
