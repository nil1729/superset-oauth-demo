# https://superset.apache.org/docs/installation/configuring-superset/#custom-oauth2-configuration
from flask_appbuilder.security.manager import AUTH_OAUTH

# Set the authentication type to OAuth
AUTH_TYPE = AUTH_OAUTH

# get the client id and secret from the environment
import os
import logging

GOOGLE_OAUTH_CLIENT_ID = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")

OAUTH_PROVIDERS = [
    {
        "name": "google",
        "token_key": "access_token",
        "icon": "fa-google",  # Icon for the provider
        "remote_app": {
            "client_id": GOOGLE_OAUTH_CLIENT_ID,
            "client_secret": GOOGLE_OAUTH_CLIENT_SECRET,
            "client_kwargs": {"scope": "openid email profile"},
            "access_token_method": "POST",
            "access_token_params": {"client_id": GOOGLE_OAUTH_CLIENT_ID},
            "jwks_uri": "https://www.googleapis.com/oauth2/v3/certs",
            "api_base_url": "https://openidconnect.googleapis.com/v1/",
            "access_token_url": "https://oauth2.googleapis.com/token",
            "authorize_url": "https://accounts.google.com/o/oauth2/auth",
        },
    }
]

# Will allow user self registration, allowing to create Flask users from Authorized User
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Gamma"

from custom_sso_security_manager import CustomSsoSecurityManager

CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager

# https://superset.apache.org/docs/installation/configuring-superset/#using-a-production-metastore
SQLALCHEMY_DATABASE_URI = (
    "postgresql://superset:password@superser-backend-db:5432/superset"
)

# load balancer
# https://superset.apache.org/docs/installation/configuring-superset/#configuration-behind-a-load-balancer
ENABLE_PROXY_FIX = True
