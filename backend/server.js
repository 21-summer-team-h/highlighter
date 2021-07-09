const execSync = require('child_process').execSync;

let VIDEO_ID = 1078156676;
let VIDEO_NAME = "test";

execSync(`./TwitchDownloader.sh ${VIDEO_ID} ${VIDEO_NAME}`)
console.log("> Download finish")