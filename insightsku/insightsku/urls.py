from django.contrib import admin
from django.urls import path
from insightskuapp import views
from insightskuapp .views import TagListView, TagCreateView, TagUpdateView, tag_delete



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.enter_client_name, name='enter_client_name'),
    path('login/', views.user_login, name='user_login'),
    path('products/', views.user_dashboard, name='products'),
    path('logout/', views.custom_logout, name='logout'),
    path('search/', views.product_search, name='product_search'),
    path('advanced_search/', views.advanced_product_search, name='advanced_product_search'),
    path('add_product/', views.add_product, name='add_product'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/add/', TagCreateView.as_view(), name='tag-add'),
    path('tags/<int:pk>/edit/', TagUpdateView.as_view(), name='tag-edit'),
    path('tags/<int:pk>/delete/', tag_delete, name='tag-delete'),
]


