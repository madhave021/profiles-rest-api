from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name='login')
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns =[


url(r'^hello-api/',views.HelloApiView.as_view()),
url(r'',include(router.urls)),

]
