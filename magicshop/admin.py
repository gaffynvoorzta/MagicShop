from django.contrib import admin
from .models import PotionItem, Ingredient, RecipeRequirement, Purchase, Reviews

# Register your models here.
admin.site.register(PotionItem)
admin.site.register(Ingredient)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)
admin.site.register(Reviews)
