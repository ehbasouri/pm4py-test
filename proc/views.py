from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import os
from django.core.files.storage import FileSystemStorage
from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.visualization.petrinet import factory as vis_factory

#handle input

def handle_uploaded_file(f):
	# os.remove('static/proc/model.png')
	fs= FileSystemStorage()
	fs.save('log.xes', f)

	# get_model()

def get_model():
	os.rename("//home/ehsan/codes/pm4py-test/media/model.png", "/home/ehsan/codes/pm4py-test/proc/static/proc/model.png")

# views !!!

def main_view(request):
    return render(request, 'proc/main.html')

def model_view(request):
    return render(request, 'proc/model.html')

def confirm_view(request):
    return render(request, 'proc/confirm.html')

def upload_file(request):
	if request.method == 'POST':
	    form = UploadFileForm(request.POST, request.FILES)
	    # get_model()
	    if form.is_valid():
	        handle_uploaded_file(request.FILES['file'])
	        return HttpResponseRedirect('/main/confirm/')
	else:
		# print('not valid !!!')
	    form = UploadFileForm()
	return render(request, 'proc/uploadFile.html', { "form": form, "image": "proc/test.png" })
