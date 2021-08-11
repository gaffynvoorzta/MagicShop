from django.shortcuts import redirect, render
from django.db.models import Sum, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import SuspiciousOperation
import random
from .models import Ingredient, PotionItem, Purchase, RecipeRequirement, Reviews
from .forms import IngredientForm, PotionItemForm, RecipeRequirementForm

# Create your views here.
def about(request):
  try:
    random_review = random.choice(Reviews.objects.all())
  except Reviews.DoesNotExist:
    raise Http404()
  context = {"review": random_review}
  return render(request, "magicshop/about.html", context)

class HomeView(TemplateView):
    template_name = "magicshop/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["potion_items"] = PotionItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context


class IngredientsView(LoginRequiredMixin, ListView):
    template_name = "magicshop/ingredients_list.html"
    model = Ingredient


class NewIngredientView(LoginRequiredMixin, CreateView):
    template_name = "magicshop/add_ingredient.html"
    model = Ingredient
    form_class = IngredientForm


class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    template_name = "magicshop/update_ingredient.html"
    model = Ingredient
    form_class = IngredientForm

class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    template_name = "magicshop/delete_ingredient.html"
    model = Ingredient
    form_class = IngredientForm
    success_url = "/ingredients"

class PotionView(LoginRequiredMixin, ListView):
    template_name = "magicshop/potion_list.html"
    model = PotionItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_dict = {}
        
        for potion in PotionItem.objects.all():
            total_cost = 0
            for requirement in potion.reciperequirement_set.all():
                total_cost += requirement.req_cost()
            total_dict[potion.id] = {'total_cost':round(total_cost, 2), 'profit_cost':round(potion.price - total_cost, 2)}
        context["total_dict"] = total_dict
        return context

class NewPotionItemView(LoginRequiredMixin, CreateView):
    template_name = "magicshop/add_potion_item.html"
    model = PotionItem
    form_class = PotionItemForm

class UpdatePotionItemView(LoginRequiredMixin, UpdateView):
    template_name = "magicshop/update_potion_item.html"
    model = PotionItem
    form_class = PotionItemForm
    success_url = "/potions"

class DeletePotionItemView(LoginRequiredMixin, DeleteView):
    template_name = "magicshop/delete_potion_item.html"
    model = PotionItem
    form_class = PotionItemForm
    success_url = "/potions"
    
class NewRecipeRequirementView(LoginRequiredMixin, CreateView):
    template_name = "magicshop/add_recipe_requirement.html"
    model = RecipeRequirement
    form_class = RecipeRequirementForm

class UpdateRecipeRequirementView(LoginRequiredMixin, UpdateView):
    template_name = "magicshop/update_recipe_requirement.html"
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    success_url = "/potions"

class DeleteRecipeRequirementView(LoginRequiredMixin, DeleteView):
    template_name = "magicshop/delete_recipe_requirement.html"
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    success_url = "/potions"

class PurchasesView(LoginRequiredMixin, ListView):
    template_name = "magicshop/purchase_list.html"
    model = Purchase


class NewPurchaseView(LoginRequiredMixin, TemplateView):
    template_name = "magicshop/add_purchase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["potion_items"] = [X for X in PotionItem.objects.all() if X.available()]
        return context

    def post(self, request):
        potion_item_id = request.POST["potion_item"]
        potion_item = PotionItem.objects.get(pk=potion_item_id)
        requirements = potion_item.reciperequirement_set
        purchase = Purchase(potion_item=potion_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect("/purchases")


class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "magicshop/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("potion_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.potion_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.price_per_unit *\
                    recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context


def log_out(request):
    logout(request)
    return redirect("home")

def login_request(request):
    #login(request.user)
    return redirect("home")
