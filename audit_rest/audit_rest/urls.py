"""audit_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from audit_rest import views


urlpatterns = [
    url(r'^show_info_port', views.show_info_port),
    url(r'^show_info_vlan', views.show_info_vlan),
    url(r'^list_nodes_all', views.list_nodes_all),
    url(r'^switch_check_port', views.switch_check_port),
    url(r'^switch_check_vlan', views.switch_check_vlan),
    url(r'^version', views.audit_version)
]

urlpatterns = format_suffix_patterns(urlpatterns)
