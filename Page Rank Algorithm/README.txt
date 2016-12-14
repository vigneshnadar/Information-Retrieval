1) Install Python 2.7.12
2) Install Pycharm
3) Open Pycharm
4) Open the Project IR HW2
   Task 1:  'Task 1 A.py'
   Task 2: 'Task 2.py'
   Inlink and Outlink Graph generating logic : 'GraphGenerator.py'
   Page Rank Algo : 'PageRank.py'
   Sequential Steps to run and store: 'TaskRunner.py'
   Other Helper Files
   'InlinkCounter.py'
   'FileDownload.py'
   'InlinkGraph.py'
5) File -> Settings -> Project : HW IR 1-> Project Interpreter ->
   Install the following packages
   a) Beautiful Soup 4
   b) HTMLPARSER
   c) urllib, urlparse
6)
STEPS TO RUN:
1) After opening the project in Pycharm
   For respective tasks run the respective files
   Task 1: Run File 'InlinkGraph.py'
   Task 2: Run File 'Task 2.py' for G2 and 'Task 1 A.py' for G1
2) After Running Task 1 the files generated are as follows
    'G1 Graph.txt'

    The crawled Urls are stored in Task 1 Bfs Crawled Urls.txt
    The format of the files is
    Depth : (Depth of Url Crawled), Rank: (Order of Url), URL: (URL Link)
    Depth denotes the depth at which the url was found
    Rank denotes Serial Number. It is the order in which files were crawled
    Url: The crawled Urls

3) After Running Task 2 the files generated are as follows
    For G1
    a) G1 Page Rank.txt
    b) G1 Perplexity.txt
    Note: The inlink graph is stored in 'G1 Graph.txt'

    For G2
    a) G2 Page Rank.txt
    b) G2 Perplexity.txt
    Note: The inlink graph is stored in 'wt2g_inlinks.txt'

4)  The explanation for Task 3 is given in 'Task 3.txt'
5) The Statistics asked for G1 and G2 are given in 'Task Statistics.txt'

7) Note: The data is appended in these files. In case you run the program once and want to re-run the program
   Delete these files and run the program


