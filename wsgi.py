from app import create_app

app, mail, socketio, csrf = create_app()

if __name__ == "__main__":
    socketio.run(app)
    # app[0].run(debug=True)