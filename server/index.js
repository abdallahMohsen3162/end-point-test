

const io = require("socket.io")(8461, {
    cors:{
        origin:"http://localhost:3000"
    }
})    
    
let mp = new Map();



io.on("connection", (socket) => {
    socket.on("send", data => {
        console.log(data);
    })

    socket.on("con", data => {
        mp.set(data, socket.id)
        console.log(mp);
    })
})  

