from django import forms

from clinic.models import Patient, Consultation


class PatientForm(forms.ModelForm):


    class Meta:
        model = Patient
        fields = ('Nom', 'Prenom', 'Gendre', 'Age', 'Date_Naissance', 'Adresse', 'Mobile', 'NSS')
        widgets = {
            'Nom': forms.TextInput(attrs={'class': 'form-control', 'minlength': '5'}),
            'Prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'Gendre': forms.Select(attrs={'class': 'form-control'}),
            'Age' : forms.TextInput(attrs={'class': 'form-control'}),
            'Date_Naissance': forms.DateInput(attrs={"data-provide":"datepicker","data-date-format":"dd/mm/yyyy" ,'class': 'form-control', 'value':'01/01/2000'}),
            'Adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'Mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'NSS': forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'Nom': 'Nom ',
            'Prenom': 'Prénom',
            'Gendre': 'Gendre',
            'Date_Naissance': 'Date Naissane',
            'Adresse': 'Adresse',
            'Mobile': 'N° Tel',
            'NSS': 'N° Securité social',
        }



class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('num', 'date', 'Diag')



