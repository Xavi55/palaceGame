from flask import Flask, render_template
from flask_socketio import SocketIO, emit, rooms,join_room, leave_room

from Game import Game

app=Flask(__name__)
app.config['SECRET_KEY']='YEK_TERCES'
socketio=SocketIO(app)

clients={} #{<room>:{'x':<name>,'o':<name>}}

@app.route('/')
def index():
    return ('<h1>TEST</h1>')



################################3
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