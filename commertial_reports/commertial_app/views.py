from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from commertial_reports.settings import *
from django.forms.models import model_to_dict
import stripe
from datetime import datetime
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "commertial_app/base.html")


def commertial_reports(request):
    reports = Users.objects.all()
    reports1 = Reports.objects.filter(analysis_type=1, user_id=46).values()
    # print(reports1)
    return render(
        request, "commertial_app/commertial_reports.html", {"reports": reports1}
    )
    # return HttpResponse("hello world")


def dscrs_reports(request):
    reports = Dscrs.objects.filter(user_id=46)
    # print(reports)
    return render(request, "commertial_app/dscr_reports.html", {"reports": reports})


def payment_method(request):
    subscription = Subscriptions.objects.filter(
        user_id=634, activation="current"
    ).last()
    user = Users.objects.get(id=634)

    plans = Plans.objects.get(id=1)
    # print(plans.id, plans.plan_name, plans.price, plans.stripe_id)
    # print(subscription)
    # if request.method == "POST":
    # if request.POST["type"] != "upgrade":
    #     firstname = request.POST.get("first_name")
    #     lastname = request.POST.get("last_name")
    #     phone = request.POST.get("phone")
    #     email = request.POST.get("email")
    #     role_id = request.POST.get("role_id")
    #     password = request.POST.get("password")
    #     plan_id = request.POST.get("plan_id")
    #     amount_paid = request.POST.get("amount")
    #     type = request.POST.get("type")
    # plans = Plans.objects.get(id=request.POST.get("plan_id"))
    return render(
        request,
        "commertial_app/payment_change.html",
        {"subscription": subscription, "plans": plans, "users": user},
    )


def AddStripePaymentMethod(request):
    user = Users.objects.get(id=634)
    print(user.stripe_id)
    if request.method == "POST":
        input = request.POST
        print(input)
        token = request.POST.get("stripeToken")
        print(token)
        request.session["change_method_subscription_id"] = request.POST.get(
            "subscription_id"
        )
    myplans_stripe = Subscriptions.objects.filter(user_id=634).last()
    request.session["plan_id"] = myplans_stripe.plan_id
    request.session["type"] = "change"
    if myplans_stripe.payment_method == 1:
        stripe.api_key = STRIPE_SECRET_KEY
        if not user.stripe_id:
            stripecustomer = stripe.Customer.create(user)
        sub = stripe.Customer.create_source(user.stripe_id, source=token)
        # print(sub["id"])
        # print(x)
        # print(sub)
        # for i in sub:
        #     print(i)
        # print(type(sub))
        new_sub = stripe.Subscription.create(
            customer=user.stripe_id,
            items=[
                {"price": myplans_stripe.stripe_plan},
            ],
        )
        # print(new_sub)
        # print(new_sub["id"])
        # for i in new_sub:
        #     print(i)
        stripe.Subscription.delete(
            myplans_stripe.stripe_id,
        )
        myplans_stripe.stripe_status = "cancel"
        myplans_stripe.save()
        new_subscription = Subscriptions.objects.create(
            user_id=myplans_stripe.user_id,
            name=myplans_stripe.name,
            stripe_id=new_sub["id"],
            stripe_status=new_sub["status"],
            stripe_plan=myplans_stripe.stripe_plan,
            quantity=new_sub["quantity"],
            ends_at=myplans_stripe.ends_at,
            expiry=myplans_stripe.expiry,
            start_date=datetime.fromtimestamp(new_sub["start_date"]).strftime(
                "%Y-%m-%d"
            ),
            trial_ends_at=myplans_stripe.trial_ends_at,
            amount_paid=myplans_stripe.amount_paid,
            payment_method=myplans_stripe.payment_method,
            payment_info=sub["last4"],
            brand=sub["brand"],
            plan_id=myplans_stripe.plan_id,
            activation=myplans_stripe.activation,
            trial_allowed=myplans_stripe.trial_allowed,
            access_allowed=myplans_stripe.access_allowed,
            cron=myplans_stripe.cron,
            created_at=myplans_stripe.created_at,
            updated_at=datetime.fromtimestamp(new_sub["start_date"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )

        messages.success(request, "You have successfully Changed your Payment Method.")
        return render(request, "commertial_app/payment_change.html")


# def addpaymentmethod_success(request):
#     user = Users.objects.get(id=634)


# def success(request):
#     return render(request, "commertial_app/success.html")
