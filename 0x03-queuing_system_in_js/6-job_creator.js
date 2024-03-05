const kue = require('kue');
const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
	phoneNumber: 'string',
  	message: 'string',
})
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error('Error creating notification job:', err);
    }
  });

job.on('complete', function(result){
  console.log('Notification job completed');
});
