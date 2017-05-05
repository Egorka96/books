from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.views import generic

from core.forms import RecordForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class View(PermissionRequiredMixin, generic.View):
    permission_required = 'core.can_open'
    template_name = 'core/index.html'


