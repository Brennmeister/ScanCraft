
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms

from ScanCraft.apps.core.models import InputFile


class InputFileForm(forms.ModelForm):
    class Meta:
        model = InputFile
        fields = '__all__'  # ()"file_input", "created_at", "updated_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'file_input', Field('created_at', read_only=True))
        self.helper.add_input(Submit('submit', 'Save'))
