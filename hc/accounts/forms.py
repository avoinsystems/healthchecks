from django import forms


class LowercaseEmailField(forms.EmailField):
    def clean(self, value):
        value = super(LowercaseEmailField, self).clean(value)
        return value.lower()


class EmailForm(forms.Form):
    email = LowercaseEmailField()
