from django import forms
from card_gds.models import CardsComment


class CardsCommentForm(forms.ModelForm):
    class Meta:
        model = CardsComment