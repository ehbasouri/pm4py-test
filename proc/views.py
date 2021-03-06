from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import os
import glob
from django.core.files.storage import FileSystemStorage
from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.visualization.petrinet import factory as vis_factory
from pm4py.algo.discovery.inductive import factory as inductive_miner
from pm4py.algo.discovery.heuristics import factory as heuristics_miner
from pm4py.algo.discovery.causal import factory as causal_miner
from pm4py.algo.discovery.dfg import factory as dfg_miner
#from pm4py.algo.discovery.simple import factory as simple_miner

#handle input

def handle_uploaded_file(f, algorithm):

    logPath2='/home/pm4py_test/logs/log.xes'
    logPath1='/home/pm4py_test/media/log.xes'
    # os.remove('static/proc/model.png')
    fs= FileSystemStorage()
    fs.save('log.xes', f)
    move_file(logPath1,logPath2)

    log = xes_importer.import_log(logPath2)
    if algorithm=="alpha":
        print(algorithm)
        net, initial_marking, final_marking = heuristics_miner.apply(log)
    elif algorithm == "inductive":
        print(algorithm)
        net, initial_marking, final_marking = inductive_miner.apply(log)
    elif algorithm == "heuristics":
        print(algorithm)
        net, initial_marking, final_marking = heuristics_miner.apply(log)
    else:
        print('error !!!')
        print(algorithm)
        return
    gviz = vis_factory.apply(net, initial_marking, final_marking)
    vis_factory.view(gviz)
    pngUris= glob.glob('/home/pm4py_test/*.png')
    gvUris= glob.glob('/home/pm4py_test/*.gv')
    modelUri='/home/pm4py_test/proc/static/proc/model.png'
    print(pngUris)
    print(gvUris)

    os.remove(gvUris[0])
    move_file(pngUris[0],modelUri)
    

	# get_model()

def move_file(path1, path2):
	os.rename(path1, path2)

# views !!!

def main_view(request):
    return render(request, 'proc/main.html')

def model_view(request):
    return render(request, 'proc/model.html')

def confirm_view(request):
    return render(request, 'proc/confirm.html')

def upload_file_alpha(request):
	if request.method == 'POST':
	    form = UploadFileForm(request.POST, request.FILES)
	    if form.is_valid():
	        handle_uploaded_file(request.FILES['file'],"alpha")
	        return HttpResponseRedirect('/main/confirm/')
	else:
	    form = UploadFileForm()
	return render(request, 'proc/uploadFile.html', { "form": form, "action": "/main/uploadfilealpha/" })

def upload_file_inductive(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # get_model()
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'],"inductive")
            return HttpResponseRedirect('/main/confirm/')
    else:
        # print('not valid !!!')
        form = UploadFileForm()
    return render(request, 'proc/uploadFile.html', { "form": form, "action":"/main/uploadfileinductive/" })

def upload_file_heuristics(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # get_model()
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'],"heuristics")
            return HttpResponseRedirect('/main/confirm/')
    else:
        # print('not valid !!!')
        form = UploadFileForm()
    return render(request, 'proc/uploadFile.html', { "form": form, "action":"/main/uploadfileheuristics/" })
