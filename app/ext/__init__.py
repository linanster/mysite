def init_ext(app):
    from app.ext.bootstrap import bootstrap
    from app.ext.mysocketio import socketio
    bootstrap.init_app(app)
    socketio.init_app(app)
