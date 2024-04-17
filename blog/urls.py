from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowNews.as_view(), name='home'),
    path('news/<int:pk>', views.ArticleView.as_view(), name='article'),
    path('news/<int:pk>/update', views.UpdateNews.as_view(), name='update'),
    path('news/<int:pk>/delete', views.DeleteNews.as_view(), name='delete'),
    path('user/<str:username>', views.UserShowAllNews.as_view(), name='user-articles'),
    path('news/add', views.CreateNews.as_view(), name='add'),
    path('about', views.abt, name='about'),
]