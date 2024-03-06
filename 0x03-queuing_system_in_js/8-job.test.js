import createPushNotificationsJobs from './8-job.js';
const { expect } = require('chai');
const kue = require('kue')

describe('createPushNotificationsJobs function', function() {
	const queue = kue.createQueue();
	before(function() {
		queue.testMode.enter();
	});

	afterEach(function() {
  		queue.testMode.clear();
	});

	after(function() {
  		queue.testMode.exit()
	});

	it ('not array', function() {
		expect(() => createPushNotificationsJobs('', queue)).to.throw('Jobs is not an array');
	});

	it('should create jobs in the queue', function() {
        	const jobs = [{ phone: '123' }, { msg: 'Hello' }];
        	createPushNotificationsJobs(jobs, queue);
        	expect(queue.testMode.jobs.length).to.equal(2);
	});
})
