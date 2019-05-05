from users.models import ManagerUser

from django import forms


class ManagerUserForm(forms.ModelForm):
    class Meta:
        model = ManagerUser

        fields = ['name', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'type': 'password'})
