
from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.visualization.petrinet import factory as vis_factory

log = xes_importer.import_log('./example-logs/exercise3.xes')
net, initial_marking, final_marking = alpha_miner.apply(log)
gviz = vis_factory.apply(net, initial_marking, final_marking)
vis_factory.view(gviz)

