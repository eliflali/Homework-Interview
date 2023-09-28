"""
This module contains a script for processing 
news data and generating an HTML report of 
the top words in each news category.

Author: Elif Lale
"""

import argparse
import logging
from logging import getLogger, FileHandler, Formatter
from json import loads
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from html_generator import HtmlPage
import string
from threading import Thread

def configure_logging(log_file):
  # Configure logging to write to both console and log files
  logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
  logger = getLogger()
  file_handler = FileHandler(log_file)
  file_handler.setFormatter(Formatter('%(levelname)s: %(message)s'))
  logger.addHandler(file_handler)
  return logger

def tokenize_headline(headline):
  # Tokenize a headline based on word boundaries
  #  and exclude stopwords and punctuation.
  tokenizer = RegexpTokenizer(r'\b[a-zA-Z]+\b')
  words = tokenizer.tokenize(headline)
  words = [word.lower() for word in words
           if word.lower() not in nltk_stopwords
           and word not in string.punctuation and len(word) > 1]
  return words

def process_category(category, data_file, result_dict):
  # Process news data for a category and count top words.
  log_file = f'logs/{category}_log.txt'
  category_logger = configure_logging(log_file)
  word_counts = {}

  with open(data_file, 'r', encoding='utf-8') as file:
    data = [loads(line) for line in file]

  for item in data:
    if item['category'] == category:
      words = tokenize_headline(item['headline'])

      for word in words:
        word = word.lower()
        word_counts[word] = word_counts.get(word, 0) + 1

  top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
  category_logger.info("Top words for category '%s': %s", category, top_words)
  result_dict[category] = '\n'.join([f'{word}: {count}' for word,
                                    count in top_words])

def extract_unique_categories(data_file):
  # Extract unique news categories from the dataset.
  categories = set()
  with open(data_file, 'r', encoding='utf-8') as file:
    data = [loads(line) for line in file]

  for item in data:
    categories.add(item['category'])

  return categories

def main():
  # Parse command line arguments
  parser = argparse.ArgumentParser(description='Process data.')
  parser.add_argument('data_file', type=str, help='Path to the dataset file')
  args = parser.parse_args()
  global nltk_stopwords 
  nltk_stopwords = set(stopwords.words('english'))

  data_file_path = args.data_file  # Use the provided dataset file path
  categories = extract_unique_categories(data_file_path)
  threads = []
  category_top_words = {}

  for category in categories:
    thread = Thread(target=process_category,
                    args=(category, data_file_path, category_top_words))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  html = HtmlPage('output.html')
  html.add_h1('Top Words in News Categories')

  for category, top_words_str in category_top_words.items():
    html.add_h1(category)
    html.add_p(top_words_str)

  html.render()

if __name__ == '__main__':
  main()
