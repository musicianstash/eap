from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    """Storage for static files"""
    bucket_name = settings.AWS_STATIC_STORAGE_BUCKET_NAME

    # This controls how the `static` template tag from `staticfiles` gets expanded
    custom_domain = settings.AWS_S3_STATIC_CUSTOM_DOMAIN


class MediaStorage(S3BotoStorage):
    """Storage for media files"""
    bucket_name = settings.AWS_MEDIA_STORAGE_BUCKET_NAME
    custom_domain = settings.AWS_S3_MEDIA_CUSTOM_DOMAIN
