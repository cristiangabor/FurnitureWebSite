from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from presentation import views

urlpatterns =[
	url(r'^$', views.show, name="show"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
