import { createClient } from 'redis';

const client = createClient();

function redisConnection() {
    client.on('connect', () => {
        console.log('Redis client connected to the server');
    });

    client.on('error', (err) => {
        console.error(`Redis client not connected to the server: ${err}`);
    });

        client.subscribe('holberton school channel');

        client.on('message', function (channel, message) {
            console.log(`${message}`);
            if (message === 'KILL_SERVER') {
                client.unsubscribe('holberton school channel');
                client.quit();
            }
        });
    }
    redisConnection();
