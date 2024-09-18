from flask import Flask
from flask_cors import CORS
from pyngrok import ngrok

# Set auth token for NgRok
# ngrok.set_auth_token("2LzA2r64GzCFxltsAfzYWWUVfOh_mkT2bS3wwL34mpfNsFU6")

def create_app(
  engine: str, user: str, password: str, host: str, database: str
) -> Flask:
  app = Flask(__name__)
  # public_url = ngrok.connect(5001).public_url
  # app.config['PUBLIC_URL'] = public_url
  CORS(app, resources={r"/*": {"origins": "*"}})
  return app