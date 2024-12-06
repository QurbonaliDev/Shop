from django.templatetags.static import static
from django.urls import path

from market import settings
from store.views import home, products, single, register, contact

urlpatterns = ([
    path('', home, name = 'name'),
    path('contact',contact, name = 'contact'),
    path('products/<slug>/',products, name = 'products'),
    path('register',register, name = 'register'),
    path('single',single, name = 'single'),
])

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)