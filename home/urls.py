from django.urls import path
from home.views import home, about_us, listings, blog, single_blog, contact

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about-us'),
    path('listings/', listings, name='listings'),
    path('blog/', blog, name='blog'),
    path('single-blog/', single_blog, name='single-blog'),
    path('contact/', contact, name='contact'),
]