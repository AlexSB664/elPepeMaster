from django.shortcuts import render

# Create your views here.
def Index(request):
	return render(request,'index.html')

def acercadeP(request):
	return render(request,'acercade.html') 

def registroU(request):
	return render(request,'registro.html')

def dashboard(request):
	return render(request,'dashboard.html')