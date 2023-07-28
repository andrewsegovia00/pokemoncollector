from django.forms import ModelForm
from .models import Attack


class AttackForm(ModelForm):
    class Meta:
        model = Attack
        fields = [
            "names",
            "types",
            "description",
            "cost",
            "damage",
        ]
