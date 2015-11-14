from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url (r'^$', 'main.views.post_list', name='post_list'),

    url (r'^admin/',include(admin.site.urls)),
]
