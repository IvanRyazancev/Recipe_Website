from django import forms

from recipe_webapp.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'cooking_time', 'ingredients', 'images', 'author', 'weight']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'preparation_steps': 'Шаги приготовления',
            'cooking_time': 'Время приготовления',
            'ingredients': 'Ингредиенты',
            'images': 'Изображение',
            'author': 'Автор',
            'weight': 'Вес'
        }
        help_texts = {
            'cooking_time': 'Укажите общее время приготовления в минутах.',
            'weight': 'Укажите вес готового блюда в граммах.'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'preparation_steps': forms.Textarea(attrs={'rows': 6}),
            'ingredients': forms.Textarea(attrs={'rows': 4}),
        }