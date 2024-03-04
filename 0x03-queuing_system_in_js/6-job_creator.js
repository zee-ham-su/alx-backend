const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '1234567890',
    message: 'Hello, this is a notification to verify your account!'
};

const job = queue.create('push_notification_code', jobData);

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notification job failed');
});

queue.on('job enqueue', (id) => {
    console.log(`Notification job created: ${id}`);
});

job.save();
