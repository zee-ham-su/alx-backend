import { createQueue } from 'kue';
import { promisify } from 'util';
import express from 'express';
import { createClient } from 'redis';


const app = express();
const client = createClient();
const queue = createQueue();

const reserveSeat = async (number) => {
    const setAsync = promisify(client.set).bind(client);
    await setAsync('available_seats', number.toString());
};

const getCurrentAvailableSeats = async () => {
    const getAsync = promisify(client.get).bind(client);
    const availableSeats = await getAsync('available_seats');
    return availableSeats ? parseInt(availableSeats) : 0;
};

app.listen(1245, () => {
    console.log('Server is running on port 1245');
});

app.get('/available_seats', async (req, res) => {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

let reservationEnabled = true;

app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save((error) => {
        if (!error) {
            res.json({ status: 'Reservation in process' });
        } else {
            res.json({ status: 'Reservation failed' });
        }
    });

    job.on('complete', (result) => {
        console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
        console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
});

app.get('/process', async (req, res) => {
    res.json({ status: 'Queue processing' });

    const currentAvailableSeats = await getCurrentAvailableSeats();
    if (currentAvailableSeats <= 0) {
        reservationEnabled = false;
    }

    const job = await queue.process('reserve_seat', async (job, done) => {
        const availableSeats = await getCurrentAvailableSeats();
        if (availableSeats <= 0) {
            done(new Error('Not enough seats available'));
        } else {
            await reserveSeat(availableSeats - 1);
            done();
        }
    });
});

reserveSeat(50);