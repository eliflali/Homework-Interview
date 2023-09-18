import threading
import logging
import json
import nltk  # Import NLTK
from bs4 import BeautifulSoup
from html_generator import HtmlPage

# Download NLTK resources (stopwords and tokenizer)
nltk.download('stopwords')
nltk.download('punkt')

# Import NLTK libraries for stopwords and tokenization
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Set up logging to write to both console and log files
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger()
file_handler = logging.FileHandler('logs/app.log')
file_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logger.addHandler(file_handler)

# Function to process news data for a category
def process_category(category, data_file, result_dict):
    # Configure logging for this category
    log_file = 'logs/{}_log.txt'.format(category)
    category_logger = logging.getLogger(category)
    category_logger.addHandler(logging.FileHandler(log_file))
    category_logger.setLevel(logging.INFO)

    word_counts = {}
    
    # Get NLTK stopwords
    nltk_stopwords = set(stopwords.words('english'))

    with open(data_file, 'r', encoding='utf-8') as file:
        data = [json.loads(line) for line in file]

        for item in data:
            if item['category'] == category:
                headline = item['headline']
                
                # Tokenize the headline using NLTK tokenizer
                words = word_tokenize(headline)
                
                for word in words:
                    word = word.lower()
                    if word not in nltk_stopwords:
                        word_counts[word] = word_counts.get(word, 0) + 1

    # Log the top 10 words for the category
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    category_logger.info("Top words for category '{}': {}".format(category, top_words))

    # Store the top words as a string in the result_dict
    result_dict[category] = "\n".join([f"{word}: {count}" for word, count in top_words])

# Main function
def main():
    data_file_path = './data/News_Category_Dataset_v3.json'  # Path to your dataset
    categories = set()

    # Extract unique categories from the dataset
    with open(data_file_path, 'r', encoding='utf-8') as file:
        data = [json.loads(line) for line in file]
        for item in data:
            categories.add(item['category'])

    # Create threads for each category
    threads = []
    category_top_words = {}  # Store top words for each category

    for category in categories:
        thread = threading.Thread(target=process_category, args=(category, data_file_path, category_top_words))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Generate HTML report
    html = HtmlPage("output.html")
    html.add_h1("Top Words in News Categories")

    for category, top_words_str in category_top_words.items():
        html.add_h1(category)
        html.add_p(top_words_str)  # Add the top words as content to the paragraph

    html.render()

if __name__ == "__main__":
    main()
