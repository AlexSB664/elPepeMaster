from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect #puedes importar render_to_response
from files.forms import UploadForm
from files.models import Document

def upload_file(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(filename = request.POST['filename'],docfile = request.FILES['docfile'])
			newdoc.save(form)
			return redirect("uploads")
	else:
		form = UploadForm()
		#tambien se puede utilizar render_to_response
		#return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
	return render(request, 'upload.html', {'form': form})