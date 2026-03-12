from django import forms
from easy_meal_challenge.recipes.models import Recipe


class RecipeCreateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title','ingredients', 'instructions', 'image_url',)

    def clean(self):
        cleaned_data = super().clean()

        ingredients = cleaned_data.get("ingredients")

        if not ingredients:
            return cleaned_data

        ingredients_list = [i.strip().lower() for i in ingredients.split("\n") if i.strip()]

        challenge = self.initial.get("challenge")

        if not challenge:
            return cleaned_data

        required = challenge.required_ingredients.lower()

        if required not in ingredients_list:
            raise forms.ValidationError(
                f"The recipe must include '{challenge.required_ingredients}'."
            )

        if len(ingredients_list) > challenge.max_ingredients:
            raise forms.ValidationError(
                f"You can only use {challenge.max_ingredients} ingredients."
            )

        return cleaned_data


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