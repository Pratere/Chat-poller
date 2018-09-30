const tmi = require('tmi.js')
var fs = require('fs')
// var $ = require('jQuery');
var cmd = require('node-cmd');
//BEFORE RUNNING, RUN THIS: npm i tmi.js
// Valid commands start with:
let commandPrefix = '!'
// Define configuration options:
let opts = {
  identity: {
    username: 'federaltaxbot',
    password: 'oauth:' + 'kksie40vo0h1fa5w1qmjhb9bl94n7s'
  },
  channels: [
    'federaltax'
  ],
}

// These are the commands the bot knows (defined below):
let knownCommands = { echo, poll, python }

// Function called when the "echo" command is issued:
function echo (target, context, params) {
  // If there's something to echo:
  if (params.length) {
    // Join the params into a string:
    const msg = params.join(' ')
    // Send it back to the correct place:
    sendMessage(target, context, msg)
  } else { // Nothing to echo
    console.log(`* Nothing to echo`)
  }
}

function poll (target, context, params) {
  // If there's something to poll:
  if (params.length) {
    // Join the params into a string:
    const msg = params.join(' ')
    // Send it back to the correct place:
    logger2.write(`${params}\n`)
  } else { // Nothing to poll
    console.log(`* Nothing to poll`)
  }
}


function python (target, context, params) {
  // var your_param = 'abc';
  var pyProcess = cmd.get('python Print.py',
              function(data, err, stderr) {
                if (!err) {
                  console.log("data from python script " + data)
                } else {
                  console.log("python script cmd error: " + err)
                  }
                }
              );
  read = fs.readFile('demofile.txt', function(err, data) {
    console.log(`${data}`)
  })
}

// Helper function to send the correct type of message:
function sendMessage (target, context, message) {
  if (context['message-type'] === 'whisper') {
    client.whisper(target, message)
  } else {
    client.say(target, message)
  }
}

// Create a client with our options:
let client = new tmi.client(opts)

// Register our event handlers (defined below):
client.on('message', onMessageHandler)
client.on('connected', onConnectedHandler)
client.on('disconnected', onDisconnectedHandler)

// Connect to Twitch:
client.connect()

var logger = fs.createWriteStream('log.txt', {
  flags: 'a' // 'a' means appending (old data will be preserved)
})
var logger2 = fs.createWriteStream('log2.txt', {
  flags: 'a' // 'a' means appending (old data will be preserved)
})


//logger.write('some data') // append string to your file

// Called every time a message comes in:
function onMessageHandler (target, context, msg, self) {
  if (self) { return } // Ignore messages from the bot

  // This isn't a command since it has no prefix:
  if (msg.substr(0, 1) !== commandPrefix) {
    // console.log(`[${target} (${context['message-type']})] ${context.username}: ${msg}`)
    logger.write(`[${target} (${context['message-type']})] ${context.username}: ${msg}"\n"`)

    return

  }

  // Split the message into individual words:
  const parse = msg.slice(1).split(' ')
  // The command name is the first (0th) one:
  const commandName = parse[0]
  // The rest (if any) are the parameters:
  const params = parse.splice(1)

  // If the command is known, let's execute it:
  if (commandName in knownCommands) {
    // Retrieve the function by its name:
    const command = knownCommands[commandName]
    // Then call the command with parameters:
    command(target, context, params)
    console.log(`* Executed ${commandName} command for ${context.username}`)
  } else {
    console.log(`* Unknown command ${commandName} from ${context.username}`)
  }
}

// Called every time the bot connects to Twitch chat:
function onConnectedHandler (addr, port) {
  console.log(`* Connected to ${addr}:${port}`)
}

// Called every time the bot disconnects from Twitch:
function onDisconnectedHandler (reason) {
  console.log(`Disconnected: ${reason}`)
  process.exit(1)
}
