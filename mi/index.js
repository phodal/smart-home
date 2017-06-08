const miio = require('miio');

// Resolve a device, resolving the token automatically if possible
const device = miio.device({ address: '192.168.199.225' })
	.then(console.log)
	.catch(console.error);
