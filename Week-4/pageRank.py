import os
import random
import re
import sys
import numpy as np
import pandas as pd

DAMPING = 0.85
SAMPLES = 10000

def main(dir):
  corpus = crawl(dir)
  
  ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
  print(f"PageRank Results from Sampling (n = {SAMPLES})")
  for page in sorted(ranks):
    print(f"  {page}: {ranks[page]:.4f}")
  
  ranks = iterate_pagerank(corpus, DAMPING)
  print(f"PageRank Results from Iteration")
  for page in sorted(ranks):
    print(f"  {page}: {ranks[page]:.4f}")

def crawl(directory):
  pages = dict()

  # Extract all links from HTML files
  for filename in os.listdir(directory):
    if not filename.endswith(".html"):
      continue
    with open(os.path.join(directory, filename)) as f:
      contents = f.read()
      links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
      pages[filename] = set(links) - {filename}

  # Only include links to other pages in the corpus
  for filename in pages:
    pages[filename] = set(
      link for link in pages[filename]
      if link in pages
    )

  return pages
  
def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

main('corpus0')    # Either corpus1, corpus2 or corpus3