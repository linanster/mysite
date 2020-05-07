def init_views(app):
    from app.views.blue_filezilla import blue_filezilla
    from app.views.blue_index import blue_index
    app.register_blueprint(blue_filezilla)
    app.register_blueprint(blue_index)
