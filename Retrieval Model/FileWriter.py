
# write term frequency to given filename
def _write_tf_to_file(filename, tf_table):
    output=''
    with open(filename, 'a') as textfile:
        for term in sorted(tf_table,key=tf_table.get,reverse=True):
            output=output+'{0} ----> {1}\n'.format(term.encode('utf-8') , str(tf_table[term]))
        textfile.write(output)

# write document frequency to given filename
def _write_df_to_file(filename, df_table):
    output=''
    doc_id=''
    df=0
    with open(filename, 'a') as textfile:
        for term, value in sorted(df_table.items()):
            for doc,df in value.items():
                doc_id=doc_id +' '+doc
            output = output + '{0} : {1} : {2}\n'.format(term.encode('utf-8'), doc_id, str(len(value)))
            doc_id=''
        textfile.write(output)

# write stopword to given filename
def _write_stopword_to_file(filename, tf_table):
    print 'Stopword creation'
    output=''
    with open(filename, 'a') as textfile:
        for term in sorted(tf_table,key=tf_table.get,reverse=True):
            output=output+'{0} ----> {1}\n'.format(term.encode('utf-8') , str(tf_table[term]))
        textfile.write(output)






#
# # write
#     output=''
#     doc_id=''
#     df=0
#     outer_c=0
#     inner_c=0
#     with open(filename, 'a') as textfile:
#         for term, value in sorted(df_table.items()):
#             for doc in value[0]:
#                 doc_id=doc_id +' '+doc
#                 print ('i:'+ str(inner_c))
#                 inner_c+=1
#                 # print doc_id
#             print ('o:' + str(outer_c))
#             outer_c+=1
#             output = output + '{0} : {1} : {2}\n'.format(term.encode('utf-8'), doc_id, str(value[1]))
#             doc_id=''
#             # for t in value:
#                 # output = output + '{0} , {1} , {2}\n'.format(term.encode('utf-8'),t[0],str(t[1]))
#         textfile.write(output)