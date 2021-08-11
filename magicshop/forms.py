from django import forms
from .models import Ingredient, PotionItem, Purchase, RecipeRequirement, Reviews


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class PotionItemForm(forms.ModelForm):
    class Meta:
        model = PotionItem
        fields = "__all__"


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = "__all__"