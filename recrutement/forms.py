from django import forms



class AppartementForm(forms.Form):
    name = forms.CharField(max_length=100)
   



class ProgForm(forms.Form):
    fa= forms.IntegerField()
    name= forms.CharField(max_length=100)
    appartements= forms.CharField()
    price= forms.FloatField()
    nbr = forms.IntegerField()
    cr = forms.CharField()
    ##


