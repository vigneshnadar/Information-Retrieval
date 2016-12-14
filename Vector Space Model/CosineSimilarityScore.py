import os
from collections import defaultdict
from FileWriter import _write_score_to_file
import math


class CosineSimilarityRank:
    DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    DIR_PATH_FILES = 'HW3 Transformed Files'

    def __init__(self):
        self.inverted_index_unigram = dict()
        self.term_weight_denom = dict()
        self.cosine_score = {}
        self._dirpath = '{0}\{1}'.format(self.DIR_PATH, self.DIR_PATH_FILES)
        self.query={}
        self.total_doc=1000
        self.calculated_tw=dict()
        self.query_tf=defaultdict()
        self.qidf=0


    # File -> String
    # Takes a filename and returns the data in the file
    def File_Parser(self, directory_path):
        parsed_output = []
        with open(directory_path, 'r') as f:
            return str(f.read())


    # GIVEN: Parsed string input from file
    # ----> Dictionary with term as key and (docid,frequency) as values
    def Indexer(self, input_text, doc_id):
        counter_i=0
        # This for loop creates inverted index for term frequency
        for word in input_text:
            if word not in self.inverted_index_unigram:
                    self.inverted_index_unigram[word]=defaultdict(int)
                    self.inverted_index_unigram[word][doc_id] += 1
            else:
                    self.inverted_index_unigram[word][doc_id] += 1



    def TdIdfDenom(self):
        # Calculate query term if.idf
        for q in self.query:
            self.query_tf[q]=math.log(float(self.total_doc)/float(len(self.inverted_index_unigram[q])))

        # Calculate query term normalization factor to be used in Cosine similarity denominator
        for q in self.query_tf:
            self.qidf+=(float(self.query_tf[q]) ** 2)

    # Calculate weight of each term in each document by using tf.idf
    def WeightNumerator(self):
        for term, value in self.inverted_index_unigram.items():
            for doc, df in value.items():
                tf = float(self.inverted_index_unigram[term][doc]) # (log (fik) +1 )
                idf = (math.log((float(self.total_doc) / len(self.inverted_index_unigram[term])),2))

                if doc not in self.calculated_tw:
                    self.calculated_tw[doc] = defaultdict(int)
                    self.calculated_tw[doc][term] = float(tf * idf)
                else:
                    self.calculated_tw[doc][term] = float(tf * idf)


    # Calculate the cosine similarity score for each document
    def NewCosineFormula(self):
        denom=0
        num=0
        for doc,value in self.calculated_tw.items():
            for term,weight in value.items():
                denom+=(float(self.calculated_tw[doc][term]) ** 2)

                if term in self.query:
                    num+=(float(self.calculated_tw[doc][term]) * self.query_tf[term])

            self.cosine_score[doc] = float(num) / (math.sqrt(denom * self.qidf))
            num=0
            denom=0


    # Integer --> Void
    # For the given n generates frequency table and docuemnt frequency table for
    # all the files in the given directory
    # Generates a stop list and generates a Zipfs curve
    def RunTask(self,query_id,query):
        self.query=query
        for filename in os.listdir(self._dirpath):
            doc_number=filename[0:-4]
            doc_number=doc_number.replace('%','')
            doc_number = doc_number.replace('.', '')
            filename = '{0}\{1}\{2}'.format(self.DIR_PATH, self.DIR_PATH_FILES, filename)
            parsed_output = self.File_Parser(filename)
            indexer_input=parsed_output.split()
            self.Indexer(indexer_input, doc_number)

        print 'Indexing done'
        self.TdIdfDenom()
        print 'TfIdfDenom done'
        self.WeightNumerator()
        print 'Weights calculated'
        self.NewCosineFormula()
        print 'Scores calculated'

        _write_score_to_file('ResultTable.txt', self.cosine_score, query_id)


query1={'global','warming','potential'}
ScoreQuery1=CosineSimilarityRank()
ScoreQuery1.RunTask(1,query1)

query2={'green','power','renewable','energy'}
ScoreQuery2=CosineSimilarityRank()
ScoreQuery2.RunTask(2,query2)

query3={'solar','energy','california'}
ScoreQuery3=CosineSimilarityRank()
ScoreQuery3.RunTask(3,query3)

query4={'light', 'bulb', 'bulbs', 'alternative', 'alternatives'}
ScoreQuery4=CosineSimilarityRank()
ScoreQuery4.RunTask(4,query4)






