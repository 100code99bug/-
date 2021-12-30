from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('add_book',views.add_book),
    path('show_book',views.show_book),
    path('modify/<int:book_id>',views.mod_book),
    path('del/<int:book_id>',views.del_book)
]
