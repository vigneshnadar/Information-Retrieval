import os
from bs4 import BeautifulSoup
import nltk
from pylab import *
from collections import defaultdict, Counter
from FileWriter import _write_tf_to_file, _write_df_to_file, _write_stopword_to_file
from RegexCleaner import transform_data
from ZipfLaw import ZipfGraphGenerator
import math
import re
from FileDownload import create_data_files


class Generate_Corpus:
    DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    DIR_PATH_FILES = 'Task 1 Downloaded Files'
    f = 'File1.txt'

    def __init__(self):
        self.inverted_index_unigram = dict()
        self.tf_unigram = {}
        self.df_unigram = {}
        self.stopword = {}
        self.tf_totat_uni={}
        self._dirpath = '{0}\{1}'.format(self.DIR_PATH, self.DIR_PATH_FILES)


    # File -> String
    # Takes a filename which has html data and returns the text information in the file
    def File_Parser(self, directory_path):
        parsed_output = []
        with open(directory_path, 'r') as f:
            file_data = f.read()
            url = file_data.split("<!", 1)[0]
            url = url.split('/').pop().split().pop()
            html_data = file_data.split("html>", 1)[1]
            print url
            soup = BeautifulSoup(html_data, "html.parser")

            for script in soup(['style', 'script', '[document]']):
                script.extract()


            raw_text = soup.find('div', attrs={"class": "mw-body"}).get_text()

            lines = (line.strip() for line in raw_text.splitlines())

            # logic to remove unwanted line breaks
            transformation_text = (phrases.strip() for line in lines for phrases in line.split(" "))

            integrated_text = ' '.join(block for block in transformation_text if block)
            integrated_text = integrated_text.lower()

            # print (integrated_text)
            parsed_output.append(url)
            parsed_output.append(integrated_text)
            return parsed_output

    # GIVEN: Parsed string input from file
    # ----> Dictionary with term as key and (docid,frequency) as values
    def Indexer(self, input_text, doc_id):
        counter_i=0
        for word in input_text:
            if word not in self.inverted_index_unigram:
                    self.inverted_index_unigram[word]=defaultdict(int)
                    self.inverted_index_unigram[word][doc_id] += 1
                    self.tf_totat_uni[word] = 1
            else:
                    self.inverted_index_unigram[word][doc_id] += 1
                    self.tf_totat_uni[word] += 1
            self.stopword[word] = float(self.tf_totat_uni[word]) * len(self.inverted_index_unigram[word])




    # Integer --> Void
    # For the given n generates frequency table and docuemnt frequency table for
    # all the files in the given directory
    # Generates a stop list and generates a Zipfs curve
    def RunTask(self, n):
        for filename in os.listdir(self._dirpath):
            filename = '{0}\{1}\{2}'.format(self.DIR_PATH, self.DIR_PATH_FILES, filename)
            parsed_output = self.File_Parser(filename)
            print 'parsing done'
            transformed_output = transform_data(str(parsed_output))
            print 'transformation done.'
            ngram_output = self.NGramGenerator(transformed_output, n)
            print 'ngram generated'

            doc_id=parsed_output[0]
            doc_id=doc_id.replace('_','')
            doc_id = doc_id.replace('-', '')
            self.Indexer(ngram_output, doc_id)
            print 'Indexing done'



        tf_table = ''
        df_table = ''

        if n == 2:
            tf_table = 'TF Bigram Table.txt'
            df_table = 'DF Bigram Table.txt'

        if n == 1:
            tf_table = 'TF Unigram Table.txt'
            df_table = 'DF Unigram Table.txt'

        if n == 3:
            tf_table = 'TF Trigram Table.txt'
            df_table = 'DF Trigram Table.txt'

        output_tf_file_name = '{0}'.format(tf_table)
        output_df_file_name = '{0}'.format(df_table)
        print 'writing tf to file'
        _write_tf_to_file(output_tf_file_name, self.tf_totat_uni)
        print 'writing df to file'
        _write_df_to_file(output_df_file_name, self.inverted_index_unigram)
        if n == 1:
            _write_stopword_to_file("Stopword List.txt", self.stopword)


        tokens = []
        count = []
        for term in sorted(self.tf_totat_uni, key=self.tf_totat_uni.get, reverse=True):
            tokens.append(str(term.encode('utf-8')))
            count.append(self.tf_totat_uni[term])
        count = array(count)
        print 'generating zipf'
        ZipfGraphGenerator(tokens, count)


    # Takes a string as input-->Gives array of string as output
    def NGramGenerator(self, parsed_out, n):
        token_array = parsed_out.split()
        ngram = []
        ngram_str = ''
        count = len(token_array)
        if n >= 2:
            count = count - (n - 1)

        i = 0
        for i in range(count):
            for k in range(i, i + n):
                if k == i:
                    ngram_str = ngram_str + token_array[k]
                else:
                    ngram_str = ngram_str + ' ' + token_array[k]

            ngram.append(ngram_str)
            ngram_str = ''
        return ngram













    def StoreTransformedData(self):
        count=1
        dir_path='HW3 Transformed Files'
        for filename in os.listdir(self._dirpath):
            filename = '{0}\{1}\{2}'.format(self.DIR_PATH, self.DIR_PATH_FILES, filename)
            parsed_output = self.File_Parser(filename)
            print 'parsing done'
            transformed_output = transform_data(str(parsed_output))

            doc_id = parsed_output[0]
            doc_id = doc_id.replace('_', '')
            doc_id = doc_id.replace('-', '')
            create_data_files(dir_path, doc_id, transformed_output, count)
            count+=1
            print count


StoreData=Generate_Corpus()
StoreData.StoreTransformedData()