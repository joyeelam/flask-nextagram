from app import app
from config import Config
from authlib.integrations.flask_client import OAuth

oauth = OAuth()

oauth.register('google',
    client_id = app.config['G_CLIENT_ID'],
    client_secret = app.config['G_CLIENT_SECRET'],
    access_token_url = 'https://accounts.google.com/o/oauth2/token',
    access_token_params = None,
    refresh_token_url = None,
    authorize_url = 'https://accounts.google.com/o/oauth2/auth',
    api_base_url = 'https://www.googleapis.com/oauth2/v1/',
    client_kwargs = {
        'scope': 'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile',
        'token_endpoint_auth_method': 'client_secret_basic',
        'token_placement': 'header',
        'prompt': 'consent'
    }
)

oauth.init_app(app)
