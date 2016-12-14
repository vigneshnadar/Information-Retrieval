
# write score of each docuement for the given query to the given filename
def _write_score_to_file(filename, tf_table, query_id):
    output=''
    rank=1
    with open(filename, 'a') as textfile:
        for term in sorted(tf_table,key=tf_table.get,reverse=True)[:100]:
            output=output+'{0} Q0 {1} {2} {3} VectorSpaceModel\n'.format(str(query_id),term.encode('utf-8'),str(rank),str(tf_table[term]))
            rank+=1
        textfile.write(output)




