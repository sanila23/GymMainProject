from django import forms
from django.forms import ModelForm,Textarea
from django.db import transaction
from gym.models import *

from .models import Bill

from .models import Store

from .models import Schedule

from .models import Diet

from .models import Member

from .models import Trainer

from .models import Consultant


from .models import LeaveRequest


class LeaveRequestForm(forms.ModelForm):  # Inherits from forms.ModelForm
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason']


class LeaveRequestForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    reason = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows': 4}))



class ConsultantForm(forms.ModelForm):
    class Meta:
        model = Consultant
        fields = '__all__'  # Adjust fields as per your model


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'  # To include all fields from the Member model in the form

class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = '__all__'  # Include all fields from the Diet model in the form

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'  # To include all fields from the Bill model in the form

