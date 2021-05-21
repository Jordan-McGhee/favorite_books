from django.urls import path
from . import views

urlpatterns = [
    path('logout', views.logout),
    path('', views.user),
    path('add', views.add_book),
    path('create', views.create_book),
    path('<int:id>', views.view_book),
    path('<int:id>/edit', views.edit_book),
    path('<int:id>/update', views.update),
    path('<int:id>/delete', views.delete_book),
    path('<int:id>/addfav', views.add_fav),
    path('<int:id>/addfav/view', views.add_fav_view),
    path('<int:id>/removefav', views.remove_fav),
    path('<int:id>/removefav/view', views.remove_fav_view)
]