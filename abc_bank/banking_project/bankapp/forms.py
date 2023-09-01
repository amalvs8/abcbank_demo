from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import Application, Branch, District


class ApplicationForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select a District", widget=forms.Select(attrs={'class': 'form-control'}))
    branch = forms.ModelChoiceField(queryset=Branch.objects.none(), empty_label="Select a Branch", widget=forms.Select(attrs={'class': 'form-control'}))
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    banking_choices = [
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
        ('cheque_book', 'Cheque Book'),
    ]
    material_provided = forms.MultipleChoiceField(choices=banking_choices, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'date_of_birth': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Enter Date of Birth'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Home Address'}),
            'account_type': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('branch')
            except (ValueError, TypeError):
                pass
