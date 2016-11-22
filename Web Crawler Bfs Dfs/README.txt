1) Install Python 2.7.12
2) Install Pycharm
3) Open Pycharm
4) Create a project and past the below 5 files in Project folder
   Task 1:  'Task 1.py'
   Task 2: 'Task 2 A.py'
   Task 3: 'Task 2 B.py'
   Task 4: 'Task 3.py'
   'FileDownload.py'
5) File -> Settings -> Project : HW IR 1-> Project Interpreter ->
   Install the following packages
   a) Beautiful Soup 4
   b) HTMLPARSER
   c) urllib, urlparse
6)
STEPS TO RUN:
1) After opening the project in Pycharm
   For respective tasks run the respective files
   Task 1: Run File 'Task 1.py'
   Task 2: Run File 'Task 2 A.py'
   Task 3: Run File 'Task 2 B.py'
   Task 4: Run File 'Task 3.py'
   'FileDownload.py' should be in same project folder
2) After Running the 4 files containing 1000 urls are generated as follows
    a) Task 1 BFS Crawled Urls.txt
    b) Task 2 A Focused Bfs Crawled Urls.txt
    c) Task 2 B Focused Bfs Crawled Urls.txt
    d) Task 3 BFS Crawled Urls.txt
 The format of the files is
Depth : (Depth of Url Crawled), Rank: (Order of Url), URL: (URL Link)
Depth denotes the depth at which the url was found
Rank denotes Serial Number. It is the order in which files were crawled
Url: The crawled Urls

7) Note: The data is appended in these files. In case you run the program once and want to re-run the program
   Delete these files and run the program


Citations:
1) Used BeautifulSoup for HTML Parsing
2) Search Engines: Information Retrieval in Practise TrevorStrohman DonaldMetzler W.BruceCroft
   Read up concepts of web crawlers from Chapter 3
3) https://www.tutorialspoint.com/data_structures_algorithms/depth_first_traversal.htm
   Understood the traversal technique of Depth first search