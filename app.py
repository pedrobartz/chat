# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['teste'] = 
socketio = SocketIO(app)


@app.route('/')
def index():

    return render_template('index.html')


@socketio.on('message_from_client')
def handle_message(data):
    print(f"Mensagem recebida: {data['msg']}")

    emit('message_to_clients', data, broadcast=True)

if __name__ == '__main__':

    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
