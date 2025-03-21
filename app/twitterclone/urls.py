# urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from django.conf import settings

from .views import (
    configuration_profile,
    delete_tweet,
    home,
    register,
    custom_logout,
    like_tweet,
    perfil_view,
    follow_user,
    get_tweet,
    comment_tweet,
    retweet,
    like_comment,
    CustomLoginView
)

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    
    # Página inicial com feed (para você / seguindo)
    path("", home, name="home"),
    
    # Autenticação (login, logout, registro)
     path(
        "login/",
        CustomLoginView.as_view(),
        name="login",
    ),
    path("logout/", custom_logout, name="logout"),
    path("register/", register, name="register"),
    
    # Perfis de usuários
    path("profile/", perfil_view, name="profile"),
    path("profile/configuration", configuration_profile, name="configuration_profile"),
    path("profile/<int:user_id>/", perfil_view, name="profile"),



    # Tweets
    path("tweet/<int:tweet_id>/", get_tweet, name="tweet"),  # Detalhes de um tweet
    path("tweet/<int:tweet_id>/comment/", comment_tweet, name="comment_tweet"),  # Comentar em um tweet
    path("tweet/<int:tweet_id>/retweet/", retweet, name="retweet"),  # Retweetar
    path("tweet/<int:tweet_id>/like/", like_tweet, name="like_tweet"),  # Curtir tweet
    path("tweet/<int:tweet_id>/delete", delete_tweet, name="delete_tweet"),
    
    # Ações relacionadas a comentários
    path("comment/<int:comment_id>/like/", like_comment, name="like_comment"),  # Curtir comentário

    # Seguir e deixar de seguir
    path("profile/<int:user_id>/follow/", follow_user, name="follow_user"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
