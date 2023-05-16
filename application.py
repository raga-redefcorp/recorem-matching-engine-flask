from flask import Flask
from dotenv import load_dotenv
from routers.prediction import router

# loads env variables
load_dotenv()

application = Flask(__name__)

app = application

# Register the router with the Flask application
app.register_blueprint(router)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
