from django import forms
from .models import *


class Loginform(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)


class Driver_registration_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'mob_no', 'driving_lisc', 'is_driver', 'username', 'password']
        widgets = {
            'is_driver': forms.CheckboxInput(attrs={'checked': 'true'})
        }

    def save(self, commit=True):
        user = super(Driver_registration_form, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class Owner_registration_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'mob_no', 'is_owner', 'username', 'email', 'password']
        widgets = {
            'is_owner': forms.CheckboxInput(attrs={'checked': 'true'})
        }

    def save(self, commit=True):
        user = super(Owner_registration_form, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class Driver_recieve_portal_form(forms.ModelForm):
    class Meta:
        model = Driver_recieve_portal
        fields = '__all__'
        exclude = ['vehicle']


class Driver_pay_portal_form(forms.ModelForm):
    class Meta:
        model = Driver_pay_portal
        fields = '__all__'
        exclude = ['vehicle']


class Add_vehicle_form(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ['username']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['vehicle']
        widgets = {
            'text': forms.Textarea
        }
