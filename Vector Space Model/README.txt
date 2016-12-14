*******************************************************
;;;;;;;;;;;;;;;;;;;LOGIC OF CODE;;;;;;;;;;;;;;;;;;;;;;;

1) Extract inverted index from HW3
2) Calculate the weights for each term in each document
   The formula used for weight calculation is tf.idf
   where tf= term frequency of term in that document
         idf= (log (total number of documents)/(no of docs in which the term occurs))
   for the query term
   tf= term frequency of term in query
   idf is same as that of terms in corpus i.e. same as above idf
3) Once the weights are calculated
   The Cosine similarity score for each document is calcuated
4) Documents are sorted as per their score
   and top 100 docs are written to a file in a particular format

*******************************************************
;;;;;;;;;;;;;;;;;RUNNING THE CODE;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;VECTOR SPACE MODEL;;;;;;;;;;;;;;;;;;;;;;

1) Install Python 2.7.12
2) Install Pycharm
3) Open Pycharm
4) Create a project and past the below files in Project folder
   'CosineSimilarityScore.py'
   'FileWriter.py'

5) File -> Settings -> Project : IR HW4 -> Project Interpreter ->
   Install the following packages
   a) math
   b) collections

6)
STEPS TO RUN:
1) After opening the project in Pycharm
   Run the File
   'CosineSimilarityScore.py' --> Creates the file ResultTable.txt


2) After Running the files are generated as follows
   1) ResultTable.txt

   The ResultTable consists of top 100 results for all 4 queries in the specified format in a single file.
   Having them in a single file will be helpful for TREC Evaluation in the next assignment
   As informed by the instructor

Note: The data is appended in these files. In case you run the program once and want to re-run the program
      Delete the above file and run the program

*******************************************************
;;;;;;;;;;;;;;;;;RUNNING THE CODE;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;LUCENE;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
Install eclipse and java
1. Open the project HW3 in eclipse
2. Run HW4.java
3. It will ask for the path where index needs to be created
   Provide it
4. After that it will ask for folder path fro which index will be created
   Provide the path for 'HW3 Transformed Files'
5. Once index is created enter 'q'
6. Now type the query for which documents need to be ranked
7. Lucene gives the top 100 documents for that query
NOTE: For each query run the program again
Also Provide a different path at which index needs to be created each time



*******************************************************
;;;;;;;;;;;;;;;;;;;CITATIONS;;;;;;;;;;;;;;;;;;;;;;;

1) Used BeautifulSoup for HTML Parsing
2) Search Engines: Information Retrieval in Practise TrevorStrohman DonaldMetzler W.BruceCroft
   Read up concepts from Chapter 7
3) https://lucene.apache.org/core/4_0_0/core/org/apache/lucene/search/similarities/TFIDFSimilarity.html
   For Comparison purposes
4) http://www.lucenetutorial.com/advanced-topics/scoring.html
   Understand the scoring of lucene

*******************************************************
