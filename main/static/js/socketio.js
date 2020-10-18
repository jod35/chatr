document.addEventListener('DOMContentLoaded',()=>{
    var socket = io.connect('http://'+ document.domain+':'+location.port);
    let room;




    //show message
    socket.on('message',(data)=>{
        const p =document.createElement('p');
        const br=document.createElement('br');

        const span_username=document.createElement('span');
        span_username.innerHTML=data.username;

        const span_timestamp=document.createElement('span');
        span_timestamp.innerHTML=data.timestamp;

        p.innerHTML=span_username.outerHTML+br.outerHTML+`${data.msg}`+br.outerHTML+span_timestamp.outerHTML;

        document.querySelector('#display-message-area').appendChild(p);
    });

    

    //send message
    document.querySelector('#send_message').onclick =()=>{
        socket.send({'msg':document.querySelector('#user_message').value,
        'username':username,'room':room})
    }

    //room selection
    document.querySelectorAll('.select-room').forEach(p => {
        p.onclick=()=>{
            let new_room=p.innerHTML;

            if (new_room ==room){
                msg=`You are already in ${room} room.`;
                printSystemMessage(msg);
            }
            else{
                leaveRoom(room);
                joinRoom(new_room);

                room=new_room;
            }
        }
    });

    function leaveRoom(room){
        socket.emit('leave',{'username':username,'room':room});
    }

    function joinRoom(room){
        socket.emit('join',{'username':username,'room':room})

        document.querySelector('#display-message-area').innerHTML="";

    }

    //Print system messages
    function printSystemMessage(msg){
        const p =document.createElement('p');
        p.innerHTML=msg;
        document.querySelector('#display-message-area').append(p);
    }
})