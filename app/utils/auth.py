import google_auth_oauthlib.flow 
import google.oauth2.credentials
import flask
from log.logger import logger

# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
#         'https://www.googleapis.com/auth/drive',
#         'https://www.googleapis.com/auth/spreadsheets']

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate_google():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'credentials.json', 
        scopes=SCOPES
    )

    flow.redirect_uri = 'http://localhost:5000/'

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
    )

    #TODO - Fix this

    authorization_response = flask.request.url
    code = flask.request.args.get('code')
    # logger.info(f'Authorization response: {authorization_response}')
    logger.info(f'Code: {code}')
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    flask.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

    return flask.session['credentials']