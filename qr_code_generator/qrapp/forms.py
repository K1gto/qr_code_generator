from django import forms
from .models import QRCode
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class QRCodeForm(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = ['link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Generate QR Code'))

