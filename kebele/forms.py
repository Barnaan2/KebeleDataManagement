from django.forms import ModelForm, widgets
from django import forms
from .models import Resident, LocalBusiness, Address

class ResidentForm(ModelForm):
    class Meta:
        model= Resident
        fields = '__all__'
        
        labels = {
            'first_name': 'Maqaa',
            'last_name': 'Maqaa Abbaa',
            'email': 'Imeeyilii',
            'username': 'Maqaa fayyadamaa',
            'password1': 'Jecha darbii',
            'password2': 'Jecha darbii mirkaneessaa',
        }
        
    # def __init__(self, *args, **kwargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})
    
    
class LocalBusinessForm(ModelForm):
    class Meta:
        model= LocalBusiness
        fields = '__all__'
        
        labels = {
            'owner': 'Abbaa Qabeenyaa',
            'name': 'Daldala',
            'type': 'Gosa ',
            'quantity': 'Baayyina',
        }
        

class AddressForm(ModelForm):
    class Meta:
        model= Address
        exclude = ['resident'] 
        
        labels = {
            'phone_number': 'Lakk bilbilaa',
            'email': 'Imeeyilii ',
            'hnum': 'Lakk Manaa ',
            'kebele': 'Ganda',
            'city': 'Magaalaa',
            'zone': 'Godina',
            'region': 'Naannoo',
        }