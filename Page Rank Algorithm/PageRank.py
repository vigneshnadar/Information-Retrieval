
from collections import  defaultdict
import math


#Calculates Page Rank
def PageRankCalculator(inlink_graph, outlink_graph,P,sink_node):
    page_rank = dict()
    new_page_rank = dict()
    set_of_dict = {}
    convergence = False
    sinkPr = 0
    iteration_count = 0
    final_count=0
    entropy = 0
    perplexity_list = []
    perplexity_store=[]
    perplexity = 0
    perplexity_change = 2
    damp_factor = 0.85
    page_count = len(P)


    for p in P:
        page_rank[p] = 1 / float(page_count)

    while (not (convergence)):
        convergence = True
        iteration_count += 1
        final_count+=1
        sinkPr = 0
        for p in sink_node:
            sinkPr += page_rank[p]

        for p in P:
            new_page_rank[p] = (1 - float(damp_factor)) / page_count
            new_page_rank[p] = new_page_rank[p] + (float(damp_factor) * sinkPr) / page_count


            for inlink in inlink_graph[p]:
                old_rank = new_page_rank[p]
                prob_out = float(page_rank[inlink]) / (len(outlink_graph[inlink]))
                new_page_rank[p] = old_rank + (float(damp_factor) * prob_out)

        for p in P:
            page_rank[p] = new_page_rank[p]

        for p in P:
            entropy += float(page_rank[p]) * math.log(float(page_rank[p]), 2.0)
        entropy *= -1
        perplexity = (pow(2.0, float(entropy)))
        perplexity_list.append(perplexity)
        perplexity_store.append(perplexity)
        entropy = 0

        if (iteration_count == 4):
            for i in range(0, 3):
                p1 = perplexity_list[i + 1]
                p2 = perplexity_list[i]
                perplexity_change = p2 - p1

                convergence = (convergence and (abs(perplexity_change) <= 1))
            perplexity_list = []
            perplexity_list.append(p1)
            iteration_count = 1
        else:
            convergence = False

        print (final_count)

    set_of_dict[0]=page_rank
    set_of_dict[1]=perplexity_store
    return set_of_dict

#Store sorted page rank values in file
def StorePageRank(filename,page_rank_store):
    with open(filename,"a") as f:
        for url in sorted(page_rank_store, key=page_rank_store.get, reverse=True):
            f.write("{s} : {v:.12f}\n".format(s=url,v=float(page_rank_store[url])))

#Store perplexity values in a file
def StorePerplexity(filename,perplexity):
    count=1
    with open(filename,"a") as f:
        for p in perplexity:
            f.write("Iteration Count: {s} , Perplexity: {v:.12f}\n".format(s=count,v=float(p)))
            count+=1












