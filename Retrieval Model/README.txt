*******************************************************
;;;;;;;;;;;;;;;;;;;LOGIC OF CODE;;;;;;;;;;;;;;;;;;;;;;;

1) Extract text from html content saved in files
   Extract only plain textual content from body
   Discard scripts and other irrelevant information
2) Parse the file and remove punctuations as specified in
   the question. Clean the data appropriately
3) From the parsed and transformed text created n grams
   for any n=1,2,3.... given by the user
4) Pass this n gram as input to indexer
   Indexer creates tf index, df index
   if n=1 also stopword is created
   All of this is later written to a file
5) Using the data from the tf index
   Zipfian curves are plotted

*******************************************************
;;;;;;;;;;;;;;;;;RUNNING THE CODE;;;;;;;;;;;;;;;;;;;;;;

1) Install Python 2.7.12
2) Install Pycharm
3) Open Pycharm
4) Create a project and past the below files in Project folder
   'GenerateTfDf.py'
   'RegexCleaner.py'
   'FileWriter.py'
   'ZipfLaw.py'
   'UnigramIndexer.py'
   'BigramIndexer.py'
   'TrigramIndexer.py'

5) File -> Settings -> Project : IR HW3 -> Project Interpreter ->
   Install the following packages
   a) Beautiful Soup 4
   b) HTMLPARSER
   c) urllib, urlparse
   d) matplotlib
   e) math
   f) nltk
   g) re
   h) __future__
   i) itertools
   j) pylab
   k)  nltk.corpus
   l) collections
6)
STEPS TO RUN:
1) After opening the project in Pycharm
   For respective tasks run the respective files
   'UnigramIndexer.py' --> Creates files for unigram
   'BigramIndexer.py'  --> Creates files for bigram
   'TrigramIndexer.py' --> Creates files for trigram
    NOTE: These 3 files just make a function call to
   'GenerateTfDf.py' with n=1,2,3
   These 3 files calls could have been in the same file
   But to reduce the load on system memory. It is advisable to
   run them seperately. If run concurrently 3 huge indexes will be
   created in memory before writing to file.


2) After Running the files are generated as follows
   1) For Unigram
    a) TF Unigram Table.txt
    b) DF Unigram Table.txt
    c) Zipfian Curve Unigram.png
    d) Stopword List.txt

   2) For Bigram
    a) TF Bigram Table.txt
    b) DF Bigram Table.txt
    c) Zipfian Curve Bigram.png

   3) For Trigram
    a) TF Trigram Table.txt
    b) DF Trigram Table.txt
    c) Zipfian Curve Trigram.png

The explanation for Stopword is present in 'Stopword Explanation.txt'

The format of TF (Term Frequency) files is
term : tf
It is sorted based on frequency in descending order

 The format of  DF (Term Frequency) files is
term : docID : df
here docid is a space seperated array of documents
it is sorted lexicographically

7) Note: The data is appended in these files. In case you run the program once and want to re-run the program
   Delete these files and run the program


*******************************************************
;;;;;;;;;;;;;;;;;;;CITATIONS;;;;;;;;;;;;;;;;;;;;;;;

1) Used BeautifulSoup for HTML Parsing
2) Search Engines: Information Retrieval in Practise TrevorStrohman DonaldMetzler W.BruceCroft
   Read up concepts for stopwords
3) https://finnaarupnielsen.wordpress.com/2013/10/22/zipf-plot-for-word-counts-in-brown-corpus/
   Used a the matplotlib to plot the zipfian curves
   provided input of tokens and frequency of tokens in sorted manner
   the respective curves were created

*******************************************************
