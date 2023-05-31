from commertial_reports.settings import *


def pub_key(request):
    return {"STRIPE_PUB_KEY": STRIPE_PUB_KEY, "STRIPE_SECRET_KEY": STRIPE_SECRET_KEY}
