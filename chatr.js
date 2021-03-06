const tmi = require('tmi.js')
var fs = require('fs')
// var $ = require('jQuery');
var cmd = require('node-cmd');
const readline = require('readline');
var events = require('events');
var eventEmitter = new events.EventEmitter();

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


//BEFORE RUNNING, RUN THIS: npm i tmi.js
// Valid commands start with:
let commandPrefix = '!'
// Define configuration options:


// These are the commands the bot knows (defined below):
let knownCommands = { poll, clear }


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

function clear () {
  var logger2 = fs.createWriteStream('currentPoll.txt', {
    flags: 'w' // 'a' means appending (old data will be preserved)
  })
  logger2.write('')
}


function python () {
  // var your_param = 'abc';
  var pyProcess = cmd.run('python Algarithm.py');
  setTimeout(function (){

    fs.readFile('topWords.txt', function(err, data) {
      console.log(`${data}`)
    })

}, 500);
}



rl.on('line', entryHandler)

// Connect to Twitch:
function entryHandler (input) {
  if (input === 'poll' || input === 'pill') {
    python()
  }
  else if (input === 'clear') {
    clear()
  }
  else if (input != '') {
    let opts = {
      identity: {
        username: 'federaltaxbot',
        password: 'oauth:' + 'kksie40vo0h1fa5w1qmjhb9bl94n7s'
      },
      channels: [
        input
      ],
    }
    let client = new tmi.client(opts)
    client.connect()

    // Register our event handlers (defined below):
    client.on('message', onMessageHandler)
    client.on('connected', onConnectedHandler)
    client.on('disconnected', onDisconnectedHandler)
  }
  else {

  }
}

var logger = fs.createWriteStream('log.txt', {
  flags: 'a' // 'a' means appending (old data will be preserved)
})
var logger2 = fs.createWriteStream('currentPoll.txt', {
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
    console.log(`[${target} (${context['message-type']})] ${context.username}: ${msg}\n`)

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
