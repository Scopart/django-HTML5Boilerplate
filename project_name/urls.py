from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.views.generic import TemplateView
from views import HomePageView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^humans/$', TemplateView.as_view(template_name="humans.txt"), name='author'),
    url(r'^$', HomePageView.as_view(), name='home'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
