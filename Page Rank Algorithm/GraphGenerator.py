from  collections import defaultdict
from PageRank import *

#read file and create inlink graph
def generate_inlinks(filename):
    my_dict = {}
    set_of_pages=set()
    set_of_dict={}

    with open(filename, 'r') as f:
        for line in f:
            items = line.split()
            key, values = items[0], items[1:]
            my_dict[key] = values
            for page in items:
                set_of_pages.add(page)

    #print my_dict
    set_of_dict[0]=my_dict
    set_of_dict[1]=set_of_pages
    return set_of_dict

#creates outlink graph from inlink graph
def generate_outlinks(inlink_graph):
    outlink_graph=defaultdict(list)
    for key,inlink in inlink_graph.items():
        for node in inlink:
           outlink_graph[node].append(key)
    return outlink_graph
    #print (outlink_graph)




def store_inlinks(inlink_graph,urls_crawled,filename,sep):
    print (len(urls_crawled))
    with open(filename, "a") as f:
        for i in urls_crawled:
            print i
            if i in inlink_graph.keys():
                f.write(i + "  " + sep.join([str(x) for x in inlink_graph[i]]) + "\n")

#generates sink nodes from outlink graph
def generate_sink_nodes(outlink_graph,P):
    sink_node = []
    for p in P:
        if p not in outlink_graph:
            sink_node.append(p)
    print (sink_node)
    return sink_node


