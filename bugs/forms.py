from django import forms  
from bugs.models import Bugs  


class registerbugs(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Bugs
		fields = "__all__"
    
