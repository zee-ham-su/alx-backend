import { expect } from 'chai';
import { createQueue } from 'kue';
import { describe, it, before, after, afterEach } from 'mocha';
import createPushNotificationsJobs from './8-job.js';

const queue = createQueue();

describe('Test createPushNotificationsJobs function', function () {
    before(function () {
        queue.testMode.enter();
    });

    afterEach(function () {
        queue.testMode.clear();
    });

    after(function () {
        queue.testMode.exit();
    });

    it('should create jobs when jobs array is provided', function () {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 4562 to verify your account'
            },
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);

        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);

        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
    });

    it('should display an error message if jobs is not an array', function () {
        expect(() => createPushNotificationsJobs('job', queue)).to.throw(Error, 'Jobs is not an array');
    });
});
