from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("logout/", views.log_out, name="logout"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('', views.HomeView.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('ingredients/', views.IngredientsView.as_view(), name="ingredients"),
    path('ingredients/new', views.NewIngredientView.as_view(), name="add_ingredient"),
    path('ingredients/<slug:pk>/update', views.UpdateIngredientView.as_view(), name="update_ingredient"),
    path('ingredients/<slug:pk>/delete', views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    path('potions/', views.PotionView.as_view(), name="potions"),
    path('potions/new', views.NewPotionItemView.as_view(), name="add_potion_item"),
    path('potions/<slug:pk>/update', views.UpdatePotionItemView.as_view(), name="update_potion_item"),
    path('potions/<slug:pk>/delete', views.DeletePotionItemView.as_view(), name="delete_potion_item"),
    path('reciperequirement/new', views.NewRecipeRequirementView.as_view(), name="add_recipe_requirement"),
    path('reciperequirement/<slug:pk>/update', views.UpdateRecipeRequirementView.as_view(), name="update_recipe_requirement"),
    path('reciperequirement/<slug:pk>/delete', views.DeleteRecipeRequirementView.as_view(), name="delete_recipe_requirement"),
    path('purchases/', views.PurchasesView.as_view(), name="purchases"),
    path('purchases/new', views.NewPurchaseView.as_view(), name="add_purchase"),
    path('reports', views.ReportView.as_view(), name="reports")
]
