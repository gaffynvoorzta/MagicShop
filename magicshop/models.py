from django.db import models

# Create your models here.
class PotionItem(models.Model):
    """
    Represents an entry off the potion list
    """
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    XLARGE = 'XL'
    SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (XLARGE, 'Extra Large'),
    ]
    title = models.CharField(max_length=200, unique=True)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default=SMALL)
    price = models.FloatField(default=0.00)
    description = models.CharField(max_length=300)
    is_restricted = models.BooleanField(verbose_name=("Restricted Item"), default = False)

    def get_absolute_url(self):
        return "/potions"
    
    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())

    def __str__(self):
        return f"{self.size} {self.title}  G.C. {self.price}"


class Ingredient(models.Model):
    """
    Represents a single ingredient in the restaurant's inventory
    """
    FAERIE = "FA"
    POISONOUS = "TX"
    NECROMANTIC = "NC"
    EXPLOSIVE = "EX"
    NONE = "--"
    RESTRICTED_CHOICES = [
        (FAERIE, "Faerie"),
        (POISONOUS, "Toxic"),
        (NECROMANTIC, "Necromantic"),
        (EXPLOSIVE, "Explosive"),
        (NONE, "---")
        ]
    EACH = "Ea"
    GRAMS = "g"
    MILLIGRAMS = "mg"
    MILLILITRES = "mL"
    LITRES = "L"
    CENTIMETRES = "cm"
    MILLIMETRES = "mm"
    LEAVES = "Lea"
    CRYSTALS = "Crs"
    DROPS = "Dps"
    CHUNKS = "Cks"
    WOTSITS = "Wts"
    UNIT_CHOICES = [
        (EACH, "Each"),
        (GRAMS, "grams"),
        (MILLIGRAMS, "milligrams"),
        (MILLILITRES, "millilitres"),
        (LITRES, "litres"),
        (CENTIMETRES, "centimetres"),
        (MILLIMETRES, "millimetres"),
        (LEAVES, "leaves"),
        (CRYSTALS, "crystals"),
        (DROPS, "pindrops"),
        (CHUNKS, "chunks"),
        (WOTSITS, "wotsits")
    ]
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES, default=EACH)
    price_per_unit = models.FloatField(default=0)
    restricted = models.CharField(max_length=2, choices=RESTRICTED_CHOICES, default=NONE)

    def get_absolute_url(self):
        return "/ingredients"
    

    def __str__(self):
        return f"""
        {self.name}, x {self.quantity},
        {self.unit},  G.C. {self.price_per_unit},
        restricted={self.restricted}
        """


class RecipeRequirement(models.Model):
    """
    Represents an ingredient required for a recipe for a MenuItem
    """
    potion_item = models.ForeignKey(PotionItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"potion_item=[{self.potion_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"
    
    def get_absolute_url(self):
        return "/potions"

    def enough(self):
        return self.quantity <= self.ingredient.quantity

    def req_cost(self):
        return round(self.quantity * self.ingredient.price_per_unit, 2)

class Purchase(models.Model):
    """
    Represents a purchase of a PotionItem
    """
    potion_item = models.ForeignKey(PotionItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"potion_item=[{self.potion_item.__str__()}]; time={self.timestamp}"

    def get_absolute_url(self):
        return "/purchases"

class Reviews(models.Model):
    """
    Represents a customer Review
    """
    ONE = "⛥"
    TWO = "⛥⛥"
    THREE = "⛥⛥⛥"
    FOUR = "⛥⛥⛥⛥"
    FIVE = "⛥⛥⛥⛥⛥"
    STAR_CHOICES = [
        (ONE, "1"),
        (TWO, "2"),
        (THREE, "3"),
        (FOUR, "4"),
        (FIVE, "5")
    ]
    reviewer = models.CharField(max_length=100)
    pentacles = models.CharField(max_length=5, choices=STAR_CHOICES, default=THREE)
    review = models.CharField(max_length = 400)

    def __str__(self):
        return f"{self.reviewer} - {self.pentacles} pentacles"