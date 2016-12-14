from bs4 import BeautifulSoup
from htmllib import HTMLParser
import re
import urllib2
import urlparse
from urllib import urlopen
from parse import *
import collections
import sys
import os
import time
from FileDownload import *


class Crawler:

    DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    DIR_PATH_FILES= 'Task 2 B Downloaded Files'

    def __init__(self):
        self._emails = []
        self._urls_visited = {}
        self._excluded = ['mailto:', 'favicon', '.ico', '.css', '.js',
                          '.jpg', '.jpeg', '.png', '.gif', '?',
                          '.pdf', '.doc', '.JPG', '.svg', ':']
        self._crawl_count = 0
        self._output = False
        self._filename = '{0}\Task 2 B Focused Dfs Crawler Urls.txt'.format(self.DIR_PATH)
        self._max_depth = 0



    @property
    def nr(self):
        return self._crawl_count

    def crawl(self, base_url, filename=None, output=False, max_depth=5):
        # reset
        self._crawl_count = 0
        self.sleep_time=1
        self._max_depth = max_depth
        self._output = output

        # strip url
        base_url = base_url.strip()
        # add http if missing
        if base_url[:7] == 'http://' or base_url[:8] == 'https://':
            pass
        else:
            base_url = 'http://{}'.format(base_url)

        # dont crawl same init url twice
        if base_url in self._urls_visited:
            return

        return self.depth_first_search(base_url)



    def depth_first_search(self, base_url, depth=1):
        if depth > self._max_depth:
            return
        if base_url in self._urls_visited:
            return
        self._urls_visited[base_url] = 1

        # politeness policy
        time.sleep(self.sleep_time)
        html = self.get_html_content(base_url)
        if not html:
            return

        # count
        self._crawl_count += 1
        # collect and write data
        self.download_file_and_store_url(base_url, html, depth)
        # get urls
        urls = self.get_urls_to_crawl(base_url, html)

        # print
        if self._output:
            self._print_output(self._crawl_count, depth)

        if self._crawl_count > 1000:
            return True

        # recursion
        for url in urls:
            self.depth_first_search(url, depth + 1)

        return True

    def download_file_and_store_url(self, base_url, html, depth):
        # As discussed in lecture the logic for downloading files is commented out below
        # Uncomment and run the file for downloading crawled files
        #create_data_files(self.DIR_PATH_FILES, base_url, html, self._crawl_count)

        # write to file: url, emails
        self._write_to_file(base_url, depth, html)

    def get_html_content(self, base_url):
        html_content = None
        try:
                req = urllib2.Request(
                    base_url, headers={'User-Agent': 'Mozilla/5.0'})
                response=urllib2.urlopen(req)
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
                html = collections.namedtuple('HTML', ['html', 'soup'])
                return html(html_string, BeautifulSoup(html_string, "html.parser"))
        except:
            return False

    def get_urls_to_crawl(self, base_url, html):
        unique_urls = []
        for url in html.soup.find_all('a'):
            href=url.text
            href=href.lower()
            url = url.get('href')
            check_url='https://en.wikipedia.org/wiki/'
            check_url=urlparse.urljoin(base_url,url)

            if url and url not in unique_urls and url != base_url and not any(word in url for word in self._excluded) and 'https://en.wikipedia.org/wiki/' in check_url.lower() and not url.startswith('#') and ('solar' in url.lower() or 'solar' in href):
                unique_urls.append(check_url)

        return unique_urls






    def _write_to_file(self, base_url, depth, html):

        with open(self._filename, 'a') as textfile:
            output = 'Depth: {0}, Rank: {1}, URL: {2}\n'.format(depth, self._crawl_count, base_url)
            textfile.write(output)





    def _print_output(self, nr, depth):
        print('Files Crawled : {0} , Depth : {1}'.format(nr, depth))


    def main(self):
        self.crawl('https://en.wikipedia.org/wiki/Sustainable_energy', 'Task 2 B Focused Dfs Crawler Urls.txt', output=True)


if __name__ == '__main__':
    Crawler().main()