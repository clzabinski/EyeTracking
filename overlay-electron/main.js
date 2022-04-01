//THIS SHIT WORKS - UNCOMMENT IF DEV DOESNT WORK
/*
const { BrowserWindow, app, screen } = require('electron')

let mainWindow = null

function main() {
    mainWindow = new BrowserWindow({
        x: 0, y: 0,
        transparent: true,
        focusable: true,
        frame: false
    })
    
    //mainWindow.setIgnoreMouseEvents(true)
    mainWindow.loadFile(`src/index.html`)
    mainWindow.maximize()
    mainWindow.on('close', event => {
        mainWindow = null
    })
}

app.on('ready', main)

// wait until ready event is fired

app.on('ready', function() {

    // get the mouse position
    let mousePos = screen.getCursorScreenPoint();
    console.log(mousePos);
});
*/
//THIS SHIT WORKS - UNCOMMENT IF DEV DOESNT WORK

//______________________________________________________//

//DEVELOPEMENT!!!!!!!!!!!!!!!!!!!!

const { BrowserWindow, app, screen } = require('electron')

let windows = Set();
let mainWindow = null;

function main() {
    mainWindow = new BrowserWindow({
        x: 0, y: 0,
        transparent: true,
        focusable: true,
        frame: false
    })
    
    //mainWindow.setIgnoreMouseEvents(true)
    mainWindow.loadFile(`src/index.html`)
    mainWindow.maximize()
    mainWindow.on('close', event => {
        mainWindow = null
    })
}

app.on('ready', main)

// wait until ready event is fired

app.on('ready', function() {

    // get the mouse position
    let mousePos = screen.getCursorScreenPoint();
    console.log(mousePos);
});