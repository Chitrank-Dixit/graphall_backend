from social.pipeline.user import USER_FIELDS
from .models import User


def create_user(strategy, details, user=None, *args, **kwargs):
    if user:
        try:
            #guest_access_token = strategy.request.META['HTTP_AUTHORIZATION'].split(" ")[1]
            #user.guest_access_token = guest_access_token
            user.save()
        except (KeyError, IndexError):
            pass
        return {'is_new': False}

    fields = dict((name, kwargs.get(name) or details.get(name))
                  for name in strategy.setting('USER_FIELDS',
                                               USER_FIELDS))
    if not fields:
        return

    fields.update({'is_active': True})
    try:
        pass
        #guest_access_token = strategy.request.META['HTTP_AUTHORIZATION']
        #fields.update({'guest_access_token': guest_access_token.split(" ")[1]})
    except (KeyError, IndexError):
        pass
    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }


def create_user_if_uid_exists(backend, details, uid, user=None, *args, **kwargs):
    if backend.name == 'facebook' and user is None:
        email = details.get('email')
        try:
            filler_email = "guest" + uid + "@flyrobe.com"
            user = User.objects.get(email=filler_email)
        except User.DoesNotExist:
            try:
                filler_email = uid + "@facebook.com"
                user = User.objects.get(email=filler_email)
            except User.DoesNotExist:
                return

        user.email = email
        user.save(update_fields=['email'])
        return {'user': user}





