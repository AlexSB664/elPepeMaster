from django.shortcuts import render

# Create your views here.
def Index(request):
	return render(request,'index.html')

#def acercade(request):
#	return render(request,'pagina/acercade.html') 