from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.views import generic

from core.forms import RecordForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from core.models import Book


class BookList(LoginRequiredMixin, generic.ListView):
    template_name = 'core/booklist.html'
    context_object_name = 'books'
    login_url = '/login'

    def get_queryset(self):
        return Book.objects.order_by('-pub_date')

book_list = BookList.as_view()


# class BookList(PermissionRequiredMixin, generic.View):
#     permission_required = 'core.can_open'
#     template_name = 'core/index.html'


