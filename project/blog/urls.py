from django.urls import path
from .views import *


urlpatterns = [
    path('new/', new_article, name='new_article'),
    path('profile/', profile, name='profile'),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),

    path('', ArticleList.as_view(), name='index'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_details'),
    path('category/<int:pk>/', ArticleListByCategory.as_view(), name='category_list'),
    path('search/', SearchResults.as_view(), name='search_results'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]


