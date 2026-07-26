from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path("create/",views.create,name="create"),
    path("edit/<int:memo_id>/",views.edit,name="edit"),
    path("delete/<int:memo_id>/",views.delete,name="delete"),
    path("search/",views.search,name="search"),
    path("category/<int:category_id>/",views.category,name="category",),
    path("register/", views.register, name="register"),
    path("profile/",views.profile, name="profile"),
]