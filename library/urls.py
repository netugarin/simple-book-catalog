from django.urls import path


from . import views
app_name = 'library'
urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('new_book/', views.book_new, name='book_new'),
    path('new_author/', views.author_new, name='author_new'),
    path('delete_book/<int:pk>', views.book_delete, name='book_delete'),
    path('delete_author/<int:pk>', views.author_delete, name='author_delete'),
]
