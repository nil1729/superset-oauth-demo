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
            # parse the email and extract username before @
            username = user_info["email"].split("@")[0]
            return {
                "name": user_info["name"],
                "email": user_info["email"],
                # make sure to return a unique username for the user
                # email is a good candidate
                # in case of SSO integration at organization level you can use the username of `username@org.domain`
                "username": username,
            }
