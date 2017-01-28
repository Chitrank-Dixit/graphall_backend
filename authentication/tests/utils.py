from datetime import timedelta
import random
from time import timezone
from django.contrib.auth.models import User
from oauth2_provider.generators import generate_client_id, generate_client_secret
from oauth2_provider.models import AccessToken, Application


class OAuthTestUtilsMixin(object):
    @staticmethod
    def get_access_token(user, application=None):
        access_token = AccessToken.objects.create(
            user=user,
            token="abc" + str(user.id).zfill(4),
            application=application if application else OAuthTestUtilsMixin.get_oauth_application(),
            expires=timezone.now() + timedelta(hours=1),
            scope="read write"
        )
        return access_token

    @staticmethod
    def get_oauth_application(client_type=Application.CLIENT_PUBLIC,
                              grant_type=Application.GRANT_IMPLICIT, name="test"):
        application, created = Application.objects.get_or_create(
            user=OAuthTestUtilsMixin.get_or_create_admin_user(),
            client_id=generate_client_id(),
            client_secret=generate_client_secret(),
            client_type=client_type,
            authorization_grant_type=grant_type,
            name=name,
            skip_authorization=True
        )

        return application

    @staticmethod
    def get_or_create_admin_user():
        admin_user, created = User.objects.get_or_create(email="admin@user.com", is_staff=True)
        return admin_user

    @staticmethod
    def create_user():
        email = "random_email_" + str(random.randint(1000000, 9999999)) + "@yahoo.com"
        create_kwargs = {
            'email': email,
        }
        return User.objects.create(**create_kwargs)

