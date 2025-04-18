from django import forms
from .models import MealLog

# Predefined food choices (you can expand this list)
FOOD_CHOICES = [
    ('apple', 'Apple'),
    ('banana', 'Banana'),
    ('chicken breast', 'Chicken Breast'),
    ('rice', 'Rice'),
    ('broccoli', 'Broccoli'),
    ('egg', 'Egg'),
    ('milk', 'Milk'),
    ('bread', 'Bread'),
    ('paneer', 'Paneer'),
    ('dal', 'Dal'),
    ('fish', 'Fish'),
    ('tofu', 'Tofu'),
    ('orange', 'Orange'),
    ('grapes', 'Grapes'),
    ('mango', 'Mango'),
    ('papaya', 'Papaya'),
    ('carrot', 'Carrot'),
    ('spinach', 'Spinach'),
    ('sweet potato', 'Sweet Potato'),
    ('potato', 'Potato'),
    ('almonds', 'Almonds'),
    ('walnuts', 'Walnuts'),
    ('cashews', 'Cashews'),
    ('raisins', 'Raisins'),
    ('peanut butter', 'Peanut Butter'),
    ('cheese', 'Cheese'),
    ('yogurt', 'Yogurt'),
    ('buttermilk', 'Buttermilk'),
    ('cucumber', 'Cucumber'),
    ('lettuce', 'Lettuce'),
    ('beetroot', 'Beetroot'),
    ('pumpkin', 'Pumpkin'),
    ('mushroom', 'Mushroom'),
    ('bell pepper', 'Bell Pepper'),
    ('onion', 'Onion'),
    ('tomato', 'Tomato'),
    ('cabbage', 'Cabbage'),
    ('cauliflower', 'Cauliflower'),
    ('green beans', 'Green Beans'),
    ('chickpeas', 'Chickpeas'),
    ('black beans', 'Black Beans'),
    ('kidney beans', 'Kidney Beans'),
    ('lentils', 'Lentils'),
    ('oats', 'Oats'),
    ('quinoa', 'Quinoa'),
    ('brown rice', 'Brown Rice'),
    ('white rice', 'White Rice'),
    ('pasta', 'Pasta'),
    ('noodles', 'Noodles'),
    ('poha', 'Poha'),
    ('upma', 'Upma'),
    ('idli', 'Idli'),
    ('dosa', 'Dosa'),
    ('sambar', 'Sambar'),
    ('chutney', 'Chutney'),
    ('paratha', 'Paratha'),
    ('chapati', 'Chapati'),
    ('naan', 'Naan'),
    ('butter', 'Butter'),
    ('ghee', 'Ghee'),
    ('honey', 'Honey'),
    ('jam', 'Jam'),
    ('cornflakes', 'Cornflakes'),
    ('muesli', 'Muesli'),
    ('protein shake', 'Protein Shake'),
    ('green tea', 'Green Tea'),
    ('black coffee', 'Black Coffee'),
    ('tea', 'Tea'),
    ('lemon water', 'Lemon Water'),
    ('smoothie', 'Smoothie'),
    ('avocado', 'Avocado'),
    ('peach', 'Peach'),
    ('plum', 'Plum'),
    ('pear', 'Pear'),
    ('kiwi', 'Kiwi'),
    ('pineapple', 'Pineapple'),
    ('watermelon', 'Watermelon'),
    ('cantaloupe', 'Cantaloupe'),
    ('jackfruit', 'Jackfruit'),
    ('sapota', 'Sapota'),
    ('guava', 'Guava'),
    ('custard apple', 'Custard Apple'),
    ('dragon fruit', 'Dragon Fruit'),
    ('fig', 'Fig'),
    ('dates', 'Dates'),
    ('soy chunks', 'Soy Chunks'),
    ('moong dal', 'Moong Dal'),
    ('urad dal', 'Urad Dal'),
    ('tur dal', 'Tur Dal'),
    ('mustard greens', 'Mustard Greens'),
    ('bitter gourd', 'Bitter Gourd'),
    ('ridge gourd', 'Ridge Gourd'),
    ('bottle gourd', 'Bottle Gourd'),
    ('brinjal', 'Brinjal'),
    ('okra', 'Okra'),
    ('drumstick', 'Drumstick'),
    ('turnip', 'Turnip'),
    ('radish', 'Radish'),
    ('spring onion', 'Spring Onion'),
    ('zucchini', 'Zucchini'),
    ('asparagus', 'Asparagus'),
    ('artichoke', 'Artichoke'),
    ('kale', 'Kale'),
    ('coconut', 'Coconut'),
]


# Predefined unit choices
UNIT_CHOICES = [
    ('grams', 'Grams'),
    ('ml', 'Milliliters'),
    ('pieces', 'Pieces'),
    ('cups', 'Cups'),
    ('tablespoons', 'Tablespoons'),
    ('teaspoons', 'Teaspoons'),
]

class MealLogForm(forms.ModelForm):
    food_name = forms.ChoiceField(choices=FOOD_CHOICES, label='Food')
    quantity = forms.FloatField(min_value=0.1, label='Quantity (e.g., 100)', help_text="Enter amount based on selected unit.")
    unit = forms.ChoiceField(choices=UNIT_CHOICES, label='Unit')
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Time')
    image = forms.ImageField(required=False, label='Upload Meal Image (Optional)')

    class Meta:
        model = MealLog
        fields = ['food_name', 'quantity', 'unit', 'time', 'image']
