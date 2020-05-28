def init_views(app):
    from app.views.blue_main import blue_main
    from app.views.blue_filezilla import blue_filezilla
    from app.views.blue_chat import blue_chat
    app.register_blueprint(blue_main)
    app.register_blueprint(blue_filezilla)
    app.register_blueprint(blue_chat)
