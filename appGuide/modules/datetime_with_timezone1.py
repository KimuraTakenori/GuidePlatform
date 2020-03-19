
from datetime import datetime
from django.utils.timezone import make_aware

def datetime_str_localize(idatetime_str, iformat = "%Y/%m/%d %H:%M"):

    idatetime_str = idatetime_str.replace('-', '/')

    return make_aware(datetime.strptime(idatetime_str, iformat))

