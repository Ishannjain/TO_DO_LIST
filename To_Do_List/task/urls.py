from django.urls import path

from . import views
urlpatterns=[
    path("",views.index,name='index'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("categories_list/",views.categories_list,name="categories_list"),
    path("create_listing/",views.create_listing,name="create_listing"),
    path("display_listing/",views.display_listing,name="display_listing"),
    path('edit/<int:listing_id>/', views.edit_listing, name='edit_listing'),
    path('delete/<int:listing_id>/', views.delete_listing, name='delete_listing')
    


]