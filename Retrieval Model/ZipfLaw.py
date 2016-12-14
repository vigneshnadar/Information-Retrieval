from __future__ import division
from itertools import *
from pylab import *
from nltk.corpus import brown
from string import lower
from collections import Counter


def ZipfGraphGenerator(tokens,counts):

    # A Zipf plot
    ranks = arange(1, len(counts) + 1)
    indices = argsort(-counts)
    frequencies = counts[indices]
    loglog(ranks, frequencies, marker=".")
    title("Zipf plot for tokens")
    xlabel("Frequency rank of token")
    ylabel("Absolute frequency of token")
    grid(True)
    for n in list(logspace(-0.5, log10(len(counts)), 20).astype(int)):
        try:
            dummy = text(ranks[n], frequencies[n], " " + tokens[indices[n]].decode('utf-8'),
                         verticalalignment="bottom",
                         horizontalalignment="left")
        except:
            print 1


    show()