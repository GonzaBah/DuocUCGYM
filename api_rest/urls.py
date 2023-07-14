from django.urls import path
from api_rest.views import webpay_plus_commit, webpay_plus_commit_error, webpay_plus_create, webpay_plus_refund, webpay_plus_refund_form

appName = 'api'

urlpatterns = [
    path('webpay_plus_create', webpay_plus_create, name='webpay_plus_create')
]