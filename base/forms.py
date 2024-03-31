# from django.forms import ModelForm
# from .models import Room

# class RoomForm(ModelForm):
#     class meta:
#         model = Room
#         fields = '__all__'

from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['host', 'participants']