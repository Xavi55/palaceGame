from flask import Flask, render_template
from flask_socketio import SocketIO, emit, rooms,join_room, leave_room

from Game import Game

app=Flask(__name__)
app.config['SECRET_KEY']='YEK_TERCES'
socketio=SocketIO(app)

clients={} #{<room>:{'x':<name>,'o':<name>}}

@app.route('/')
def index():
    return render_template('index.html')
#########################
@socketio.on('makeRoom')
def handle(data):
    name=data['name']
    room=data['room']

    if room in clients:
        emit('err',{'mess':'room {} already exists'.format(room)})
    else:
        join_room(room)
        clients[room]=Game()#new game
        clients[room].addPlayer(name)
        #clients[room]={'p{}'.format(len(game.players)):name}
        emit('joined',{'mess':'player joined'})
        status(room)
@socketio.on('joinRoom')
def handle(data):
        name=data['name']
        room=data['room']

        if room in clients:
            if len(clients[room].players) == 4:
                emit('err',{'mess':'room {} is full'.format(room)})
            else:
                join_room(room)
                clients[room].addPlayer(name)
                #clients[room]={'p{}'.format(len(game.players)):name}
                emit('joined',{'mess':'player joined'})
                status(room)
        else:
            emit('err',{'mess':'room {} does not exist'.format(room)})
##########################
def status(room):
    print('total rooms',clients)
    print('players in room: {} - {}'.format(room,len(clients[room].players)))
##########################
if __name__ == '__main__':
    socketio.run(app,debug=True)

'''
g=Game()
g.currentStack.add('3S')
g.currentStack.add('3S')
g.currentStack.add('3S')
a=g.calcCards(g.currentStack.top(),'3S')
print(a)
'''