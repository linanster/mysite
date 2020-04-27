def init_views(app):
    from app.views.blue_filezilla import blue_filezilla
    app.register_blueprint(blue_filezilla)
