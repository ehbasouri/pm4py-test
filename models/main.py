
from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.visualization.petrinet import factory as vis_factory
from pm4py.algo.discovery.inductive import factory as inductive_miner
from pm4py.algo.discovery.heuristics import factory as heuristics_miner

logPath='../logs/Chapter_1/running-example-just-two-cases.xes'
logPath2=''
log = xes_importer.import_log(logPath)
net, initial_marking, final_marking = heuristics_miner.apply(log)
gviz = vis_factory.apply(net, initial_marking, final_marking)
try:
    vis_factory.view(gviz)
except:
    print('gviz error !!!')


print("well done !!!")

