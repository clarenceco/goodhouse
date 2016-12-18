from django.conf.urls import url
from gh_app import views
from views import *

urlpatterns = [
	url(r'^$',HomePageView, name='homepageview'),
	#url(r'^list/', views.list, name='list'),
]

# urlpatterns = patterns('gh_app.views',
#     url(r'^list/$', 'list', name='list'),
# )