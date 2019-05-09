from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import os

#handle input

def handle_uploaded_file(f):
	print(f)
    # with open('some/file/name.txt', 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)
def get_model():
	print('model!!!!')
	os.rename("/home/ehsan/codes/test/test2/ehsan.png", "/home/ehsan/codes/test/test1/test.txt")
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
	    	# print('fileeeeee')
	    	# print(request.FILES['file'])
	        # handle_uploaded_file(request.FILES['file'])
	        print('file')
	        print(request.FILES['file'])
	        return HttpResponseRedirect('/main/home/')
	    else:
	        return HttpResponseRedirect('/main/confirm/')
	else:
		# print('not valid !!!')
	    form = UploadFileForm()
	return render(request, 'proc/uploadFile.html', { "form": form, "image": "proc/test.png" })
