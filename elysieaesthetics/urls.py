from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('products/', views.products, name='products'),
    path('contacts/', views.contacts, name='contacts'),
    path('price/', views.price, name='price'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('google813dd604dc222326.html', TemplateView.as_view(template_name='google813dd604dc222326.html')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
