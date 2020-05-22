from flask import Flask

app = Flask(__name__)

from views.api import api
app.register_blueprint(api)

from views.site import site
app.register_blueprint(site)

if __name__ == '__main__':
    app.run(debug=True)

