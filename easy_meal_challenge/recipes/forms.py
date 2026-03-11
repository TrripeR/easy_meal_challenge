from django import forms
from easy_meal_challenge.recipes.models import Recipe


class RecipeCreateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title','ingredients', 'instructions', 'image_url',)

    def clean_ingredients(self):
        ingredients = self.cleaned_data['ingredients']

        ingredients_list = [i.strip() for i in ingredients.split("\n") if i.strip()]

        challenge = self.initial.get('challenge')

        if challenge and len(ingredients_list) > challenge.max_ingredients:
            raise forms.ValidationError(f"You can only use {challenge.max_ingredients} ingredients.")

        return ingredients


class RecipeUpdateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title','ingredients', 'instructions', 'image_url',)


class RecipeDeleteForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance