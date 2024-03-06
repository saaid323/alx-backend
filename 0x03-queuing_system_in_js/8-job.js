
export default function createPushNotificationsJobs(list, queue) {
	if (!Array.isArray(list)) {
		throw new Error('Jobs is not an array');
	}
	for (const job of list) {
		const jobs = queue.create('push_notification_code_3', job).save(function(err){
			if (!err) {
				console.log('Notification job created: ', jobs.id)
			} else {
				console.log(`Notification job ${jobs.id} failed: ${err}`);
			}
		});
		jobs.on('complete', function(){
			console.log(`Notification job ${jobs.id} completed`);
		}).on('progress', function(progress, data){
			console.log(`Notification job ${jobs.id} ${progress}% complete`);
		});
	}
}
