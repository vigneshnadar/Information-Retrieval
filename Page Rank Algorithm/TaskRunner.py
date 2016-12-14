from GraphGenerator import *

def runtask(inlink_filename,pagerank_filename,perplexity_filename):
    # Generate inlinks
    dict_of_dict = generate_inlinks(inlink_filename)

    # Inlink Data
    inlink_data = dict_of_dict[0]

    # Set of Pages
    P = dict_of_dict[1]

    # no_inlink = {}
    empty_keys = [k for k, v in inlink_data.iteritems() if not v]

    print ("No inlink" + str(len(empty_keys)))

    # Get Outlink graph
    outlink_graph = generate_outlinks(inlink_data)

    # Generate sink nodes
    sink_node = generate_sink_nodes(outlink_graph, P)
    print ("Sink Node Count" + str(len(sink_node)))

    # Get Page Rank Values
    page_rank_perplexity = PageRankCalculator(inlink_data, outlink_graph, P, sink_node)
    page_rank = page_rank_perplexity[0]
    perplexity = page_rank_perplexity[1]

    # Store Page Rank Values
    StorePageRank(pagerank_filename, page_rank)

    # Store Perplexity
    StorePerplexity(perplexity_filename, perplexity)
