from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import RegisterForm, ProfileEditForm, CustomPasswordChangeForm
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
    path("profile/edit/",views.profile_edit,name="profile_edit"),
    path("password_change/", auth_views.PasswordChangeView.as_view(
        template_name="smartmemo/password_change.html",
        form_class=CustomPasswordChangeForm,
        success_url="/password_change/done/",
        ),name="password_change",),
    path("password_change/done/",
         auth_views.PasswordChangeDoneView.as_view(
             template_name="smartmemo/password_change_done.html",
         ),
         name="password_change_done",
         ),
]