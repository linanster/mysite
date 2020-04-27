def init_views(app):
    from app.views.blue_filemgr import blue_filemgr
    app.register_blueprint(blue_filemgr)
