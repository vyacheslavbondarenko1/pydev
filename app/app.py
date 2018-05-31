import os
from flask import Flask
from controllers import home


def setup_app():
    app = Flask(__name__)
    app.register_blueprint(home, url_prefix='/')

    return app

application = setup_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3031))
    application.run('0.0.0.0', port=port, debug=os.environ.get('FLASK_DEBUG', False))
