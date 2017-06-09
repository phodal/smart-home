#!/usr/bin/node

/* eslint-disable */

// Set path to node modules miio
const miio = require('miio');

// No need to change any lines in this section
var deviceip = process.argv[2];
var secondarg = process.argv[3];
var thirdarg = process.argv[4];

function exit() {
    process.exit(-1);
}

// Power On (on / off specified as true or false)
if (secondarg === "power") {
    setTimeout(exit, 7000);
    console.log('Sending Power', thirdarg, 'command');
    miio.device({
        address: deviceip
    }).then(device => {
        return device.setPower(JSON.parse(thirdarg));
    })
}

// Status
if (secondarg === "status") {
    miio.device({
        address: deviceip
    }).then(device => {
        stats = device.getProperties(['power'])
        console.log(stats.power);
        process.exit();
    })
}

// Specify favorite manual fan speed (1 to 16) eg usage: fanspeed 16
if (secondarg === "fanspeed") {
    setTimeout(exit, 7000);
    console.log('Setting manual fan speed to: ', thirdarg);
    miio.device({
        address: deviceip
    }).then(device => {
        return device.setFavoriteLevel(parseInt(thirdarg));
    })
}

// Set fan mode option, specify: idle, auto, silent or favorite which needs to be set for manual speed control
if (secondarg === "fanmode") {
    setTimeout(exit, 7000);
    console.log('Telling device to use', thirdarg, 'fan speed mode');
    miio.device({
        address: deviceip
    }).then(device => {
        return device.call('set_mode', [thirdarg])
    })
}

// Control the device led (specify as bright, dim or off)
if (secondarg === "led") {
    setTimeout(exit, 7000);
    console.log('Setting device led to: ', thirdarg);
    miio.device({
        address: deviceip
    }).then(device => {
        return device.setLedBrightness(thirdarg);
    })
}

// Switch the device buzzer on or off (specify as true or false)
if (secondarg === "buzzer") {
    setTimeout(exit, 7000);
    console.log('Setting device buzzer to: ', thirdarg);
    miio.device({
        address: deviceip
    }).then(device => {
        return device.setBuzzer(JSON.parse(thirdarg));
    })
}
