from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from mezzanine.core.views import direct_to_template

from .views import MakePurchase

urlpatterns = patterns("",
    # url("^$", direct_to_template, {"template": "add_purchase.html"}, name="add"),
    url("^$", MakePurchase.as_view(), name="add"),
    url("^success", direct_to_template, {"template": "success.html"}, name="success"),
)