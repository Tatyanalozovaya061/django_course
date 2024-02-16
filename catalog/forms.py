from django import forms
from django.core.exceptions import PermissionDenied

from catalog.models import Product, Version


class UserPassesTestMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func(request.user):
            # Действия, если пользователь не проходит проверку
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def test_func(self, user):
        # Реализуйте свою логику проверки здесь
        # В этом примере, пользователь должен быть модератором или владельцем
        return user.is_authenticated and (user.is_moderator or self.is_owner(user))

    def is_owner(self, user):
        # Реализуйте свою логику проверки владельца здесь
        # Здесь предполагается, что у модели есть поле "owner", содержащее владельца
        return user == self.get_object().owner


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)
        # fields = ('name', 'description', 'image', 'category', 'price', 'is')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in banned_words:
            if word in cleaned_data:
                raise forms.ValidationError('Такие слова нельзя использовать в названии продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in banned_words:
            if word in cleaned_data:
                raise forms.ValidationError('Такие слова нельзя использовать в названии продукта')
        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        # fields = ('product', 'version_number', 'version_name', 'is_active',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'