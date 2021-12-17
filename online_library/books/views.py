from django.shortcuts import render
from books.models import Book


def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    data = Book.objects.all().order_by('pub_date')
    context = {'books': data}
    if pub_date:
        data = data.filter(pub_date=pub_date)
        all_dates = Book.objects.values_list('pub_date').order_by('pub_date')
        all_dates_list = [i[0] for i in all_dates]
        index = all_dates_list.index(pub_date.date())
        prev_page = all_dates_list[index - 1].strftime('%Y-%m-%d') if index != 0 else None
        next_page = all_dates_list[index + 1].strftime('%Y-%m-%d') if index < len(all_dates_list) - 1 else None

        context = {
            'books': data,
            'prev_page': prev_page,
            'next_page': next_page
        }
    return render(request, template, context)
