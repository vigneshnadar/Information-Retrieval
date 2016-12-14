from TaskRunner import runtask

inlink_filename="wt2g_inlinks.txt"
pagerank_filename="G2 Page Rank.txt"
perplexity_filename="G2 Perplexity.txt"

#Generates inlink file, stores page rank and stores perplexity
runtask(inlink_filename,pagerank_filename,perplexity_filename)