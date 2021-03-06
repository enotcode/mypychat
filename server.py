from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)


@app.route('/')
def chat():
    return render_template('chat.html')


def messageRecived():
    print('message was received!')


@socketio.on('my event')
def handle_my_custom_event(json):
    socketio.emit('my response', json, callback=messageRecived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
