# from timeout import timeout
from bs4 import BeautifulSoup
from htmllib import HTMLParser
import re
from urllib import urlopen
import urllib2
import urlparse
import collections
import sys
import os
from FileDownload import *
import time


class Crawler:
    DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    DIR_PATH_FILES = 'Task 2 A Downloaded Files'
    CRAWLED_FILES = 'Task 2 A Focused Bfs Crawled Urls.txt'

    def __init__(self):
        self.sleep_time = 1
        self.urls_crawled = {}
        self.exclude_content = ['mailto:', 'favicon', '.ico', '.css', '.js',
                                '.jpg', '.jpeg', '.png', '.gif', '?',
                                '.pdf', '.doc', '.JPG', '.svg', ':']
        self._crawl_count = 0
        self._output = False
        self._filename = '{0}\{1}'.format(self.DIR_PATH, self.CRAWLED_FILES)
        self._max_depth = 0

    @property
    def nr(self):
        return self._crawl_count

    def crawl(self, base_url, filename=None, output=False, max_depth=5):
        # reset
        self._crawl_count = 0
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
        if base_url in self.urls_crawled:
            return

        return self.breadth_first_search(base_url)

    def breadth_first_search(self, base_url):
        # new queue
        queued_urls = collections.deque()
        # depth
        depth = 1
        # enqueue and visit first url
        self.urls_crawled[base_url] = 1
        # store url and depth
        queued_urls.append(base_url)
        queued_urls.append(depth)

        while len(queued_urls):
            if depth > self._max_depth:
                return True
            # dequeue url
            base_url = queued_urls.popleft()
            depth = queued_urls.popleft()

            # get html
            html = self.get_html_content(base_url)
            if not html:
                continue

            # count
            self._crawl_count += 1
            # check for 1000 crawled links
            if self._crawl_count > 1000:
                return True
            # write the crawled links in files and download files
            self.download_file_and_store_url(base_url, html, depth)
            # get urls
            urls = self.get_urls_to_crawl(base_url, html)

            # print
            if self._output:
                self._print_output(
                    self._crawl_count, depth)

            # enqueue and visit urls
            # increase depth while getting links inside a webpage
            depth += 1
            for url in urls:
                if url not in self.urls_crawled:
                    self.urls_crawled[url] = 1
                    queued_urls.append(url)
                    queued_urls.append(depth)

        return True

    def download_file_and_store_url(self, base_url, html, depth):
        # As discussed in lecture the logic for downloading files is commented out below
        # Uncomment and run the file for downloading crawled files
        # create_data_files(self.DIR_PATH_FILES, base_url, html, self._crawl_count)
        self._write_to_file(base_url, depth)

    def get_html_content(self, base_url):
        html_content = None

        try:
            # Politeness policy
            time.sleep(self.sleep_time)
            req = urllib2.Request(
                base_url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib2.urlopen(req)
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            html = collections.namedtuple('HTML', ['html', 'soup'])
            return html(html_string, BeautifulSoup(html_string, "html.parser"))
        except:
            return False

    def get_urls_to_crawl(self, base_url, html):
        urls_unique = []
        for url in html.soup.find_all('a'):
            href = url.text
            href = href.lower()
            url = url.get('href')
            check_url = 'https://en.wikipedia.org/wiki/'
            check_url = urlparse.urljoin(base_url, url)

            # check for unique urls, keyword solar and discard administrative links
            if url and url not in urls_unique and url != base_url and not any(word in url for word in self.exclude_content) and 'https://en.wikipedia.org/wiki/' in check_url.lower() and not url.startswith('#') and ('solar' in url.lower() or 'solar' in href):
                urls_unique.append(check_url)

        return urls_unique

    def _write_to_file(self, base_url, depth):
        # write
        with open(self._filename, 'a') as textfile:
            output = 'Depth: {0}, Rank: {1}, URL: {2}\n'.format(depth, self._crawl_count, base_url)
            textfile.write(output)

    def _print_output(self, nr, depth):
        print('Files Crawled: {0} , Depth: {1}'.format(nr, depth))

    def main(self):

        self.crawl('https://en.wikipedia.org/wiki/Sustainable_energy', 'Task 2 A Focused Bfs Crawled Urls.txt', output=True)


if __name__ == '__main__':
    Crawler().main()