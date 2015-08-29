from flask import render_template, send_from_directory
from flaskapp import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:resource>')
def serve_static_resource(resource):
    return send_from_directory('static/', resource)


@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"