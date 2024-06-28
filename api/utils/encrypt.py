from django.conf import settings
import hashlib


def md5(data_string):
    # 使用Django的KEY
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()