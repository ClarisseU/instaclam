from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^$login/$', auth_views.login,{'':'registration/login.html'},name='login'),
    url(r'^logout/$',auth_views.logout,{'next_page':'/'}),
    # url(r'$registration/$',auth_views.registration,{'':'registration/registration.html'}, name='registration'),
    url(r'^new/post$',views.new_post, name ='new-post'),
    url(r'^new/profile', views.nu_profile,name='profile'),
    url(r'^new/nuprofile', views.profile,name='profiles'),
    url(r'^search',views.search, name='search')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)