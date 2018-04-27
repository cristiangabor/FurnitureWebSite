from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def show(request):

	context_dict = {'boldmessage': 'Crunchy cream cookie candy!'}


	return render(request, 'presentation/index.html', context=context_dict)
	
