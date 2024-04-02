"""
URL configuration for Recipe_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from recipe_webapp import views
from recipe_webapp.views import RecipeEditView, RecipeDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('any_recipe/', views.any_recipe, name='any_recipe'),
    path('recipe/edit/<int:pk>/', RecipeEditView.as_view(), name='recipe_edit'),
    path('recipe/delete/<int:pk>/', RecipeDeleteView.as_view(), name='recipe_delete'),

    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)