from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    missing_mail = forms.EmailField(required=True)
    contact_mail = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for key, _ in self.fields.items():
            self.fields[key].widget.attrs.update({"class": "input is-primary"})

class FindPersonForm(forms.Form):
    key = forms.CharField(max_length=50, required=True)
    def __init__(self, *args, **kwargs):
        super(FindPersonForm, self).__init__(*args, **kwargs)
        for key, _ in self.fields.items():
            self.fields[key].widget.attrs.update({"class": "input is-primary"})
