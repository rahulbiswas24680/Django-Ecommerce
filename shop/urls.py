from django.urls import path
from shop.views import HomeListView, ProductListView, ProductDetailView, contact, about

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('<slug:category_slug>/', ProductListView.as_view(), name='category-products'),
    path('<int:id>/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    
]
