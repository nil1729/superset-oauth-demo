import logging
from superset.security import SupersetSecurityManager


class CustomSsoSecurityManager(SupersetSecurityManager):

    def oauth_user_info(self, provider, response=None):
        if provider == "google":
            # this line request a GET to base_url + '/' + userinfo with Bearer  Authentication,
            # and expects that authorization server checks the token, and response with user details
            # https://openidconnect.googleapis.com/v1/userinfo
            user_info_response = self.appbuilder.sm.oauth_remotes[provider].get(
                "userinfo"
            )
            user_info = user_info_response.json()
            return {
                "name": user_info["name"],
                "email": user_info["email"],
                "username": user_info["email"],
            }
