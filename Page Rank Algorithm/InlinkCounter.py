from GraphGenerator import *

def runtask(inlink_filename):
    # Generate inlinks
    dict_of_dict = generate_inlinks(inlink_filename)

    # Inlink Data
    inlink_data = dict_of_dict[0]
    # P=['WT21-B37-76','WT21-B37-75','WT25-B39-116','WT23-B21-53','WT24-B40-171']
    # P = ['Main_Page', 'Brazil', 'Integrated_Authority_File', 'Digital_object_identifier', 'International_Standard_Book_Number']
    inlink_count={}
    for k,v in inlink_data.items():
        inlink_count[k]=len(v)
    count=0
    for inlink in sorted(inlink_count, key=inlink_count.get, reverse=True):
        print (str(inlink)+": "+str(inlink_count[inlink]))
        count+=1
        if(count>5):
            return

runtask("wt2g_inlinks.txt")
# runtask("G1 Graph.txt")

