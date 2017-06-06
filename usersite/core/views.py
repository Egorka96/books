from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from core.models import Book


class BookList(LoginRequiredMixin, generic.ListView):
    template_name = 'core/booklist.html'
    context_object_name = 'books'
    login_url = '/login'

    def get_queryset(self):
        return Book.objects.order_by('-pub_date')

book_list = BookList.as_view()


class BookEdit(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'core.change_book'
    template_name = 'core/bookedit.html'
    model = Book
    fields = '__all__'
    success_url = '/'
edit = BookEdit.as_view()


