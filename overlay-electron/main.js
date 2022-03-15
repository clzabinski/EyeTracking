// const { app, BrowserWindow } = require('electron')
// require('@electron/remote/main').initialize()

// function createWindow() {
//     // Create the browser window.
//     const win = new BrowserWindow({
//         width: 800,
//         height: 600,
//         webPreferences: { nodeIntegration: true, contextIsolation: false }
//     })

//     // Load the index.html of the app.
//     win.loadFile('src/index.html')

//     // Open the DevTools.
//     win.webContents.openDevTools()
// }

// // This method will be called when Electron has 
// // finished initialization and is ready to create
// // browser windows. Some APIs can only be used 
// // after this event occurs. This method is 
// // equivalent to 'app.on('ready', function())'
// app.whenReady().then(createWindow)

// // Quit when all windows are closed.
// app.on('window-all-closed', () => {

//     // On macOS it is common for applications and 
//     // their menu bar to stay active until the user 
//     // quits explicitly with Cmd + Q
//     if (process.platform !== 'darwin') {
//         app.quit()
//     }
// })

// app.on('activate', () => {
//     // On macOS it's common to re-create a window in the 
//     // app when the dock icon is clicked and there are no 
//     // other windows open.
//     if (BrowserWindow.getAllWindows().length === 0) {
//         createWindow()
//     }
// })

// In this file, you can include the rest of your 
// app's specific main process code. You can also 
// put them in separate files and require them here.


//___________________________________________________________________

// const { app, BrowserWindow } = require('electron')

// const createWindow = () => {
//     const win = new BrowserWindow({
//         x: 0, y: 0,
//         transparent: true,
//         frame: false,
//         focusable: false
//     })
//     // win.setIgnoreMouseEvents(true)
//     win.loadFile('src/index.html')
//     win.maximize()
//     //win.show()
// }
// app.whenReady().then(() => {
//     createWindow()
// })

const { BrowserWindow, app } = require('electron')

let mainWindow = null

function main() {
    mainWindow = new BrowserWindow({
        x: 0, y: 0,
        transparent: true,
        focusable: false,
        frame: false
    })
    mainWindow.setIgnoreMouseEvents(true)
    mainWindow.loadFile(`src/index.html`)
    mainWindow.on('close', event => {
        mainWindow = null
    })
}

app.on('ready', main)