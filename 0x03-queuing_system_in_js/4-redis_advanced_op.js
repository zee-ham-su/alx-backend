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

function createHash() {
    client.hset('HolbertonSchools', 'Portland', 50, print);
    client.hset('HolbertonSchools', 'Seattle', 80, print);
    client.hset('HolbertonSchools', 'New York', 20, print);
    client.hset('HolbertonSchools', 'Bogota', 20, print);
    client.hset('HolbertonSchools', 'Cali', 40, print);
    client.hset('HolbertonSchools', 'Paris', 2, print);
}


function displayHash() {
    client.hgetall('HolbertonSchools', (err, obj) => {
        if (err) {
            console.error(`Error retrieving hash values: ${err}`);
        } else {
            console.log('Hash values retrieved:');
            console.log(obj);
        }
    });
}

redisConnection();

createHash();

displayHash();