from django import forms

contact_type = [
    ("question", "Question"),
    ("suggestion", "Suggestion"),
]

class AdoptionForm(forms.Form):
    nom = forms.CharField(label='Nom', widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(label='Prenom', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cin = forms.CharField(label='CIN', widget=forms.TextInput(attrs={'class': 'form-control'}))
    salair_men = forms.IntegerField(label='Salaire mensuelle', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    logement = forms.BooleanField(label='Logement (avec ou sans jardin)',widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    adresse = forms.CharField(label='Adresse', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.IntegerField(label='Téléphone', widget=forms.NumberInput(attrs={'class': 'form-control'}))

class ContactForm(forms.Form):
    typeContactForm = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=contact_type,
        label='Objet de message',
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    sender = forms.EmailField( label='Email',widget=forms.EmailInput(attrs={'class': 'form-control'}))
