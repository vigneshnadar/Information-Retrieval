from TaskRunner import runtask

inlink_filename="G1 Graph.txt"
pagerank_filename="G1 Page Rank.txt"
perplexity_filename="G1 Perplexity.txt"

#Generates inlink file, stores page rank and stores perplexity
runtask(inlink_filename,pagerank_filename,perplexity_filename)