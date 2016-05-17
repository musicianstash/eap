from django.contrib.auth.signals import user_logged_in


def sync_from_mailchimp(sender, user, request, **kwargs):
    # todo: get Newsletter and call sync_from_mailchimp
    pass

# after user logs in synchronize his subscription settings
user_logged_in.connect(sync_from_mailchimp)