from flask import Flask
from apis import login, user_provider, conversation, summary
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

"""
This file is the entry point of the application.
It initializes the Flask app and registers the different blueprints for routing

"""

app.register_blueprint(login.login_bp)
app.register_blueprint(user_provider.userprovider_bp)
app.register_blueprint(conversation.conversation_bp)
app.register_blueprint(summary.summary_bp)

# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Project API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run()
