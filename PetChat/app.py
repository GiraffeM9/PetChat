# main app - file runs the whole website backend
from website import create_app


if __name__ == "__main__":
    app, socketio = create_app()
    socketio.run(app, debug=True)
