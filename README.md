# News Category Analyzer

## Overview

The News Category Analyzer is a Python script that processes news data and generates an HTML report of the top words in each news category. It is designed to work with a dataset containing news articles.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- **Python 3.x**
- **NLTK** library (`nltk`)
- **BeautifulSoup** library (`beautifulsoup4`)

You can install the required Python packages using `pip`:

```bash
pip install nltk beautifulsoup4
```


## Usage

### 1. Prepare Your Dataset
Download and store your news dataset in a JSON format. The script assumes the dataset contains information about news articles, including their headlines and categories.

### 2. Run the Script
Open your terminal and navigate to the script's directory. Run the script using the following command, replacing your_dataset.json with the path to your dataset file:

```bash
python main.py your_dataset.json
```

The script will process the data, create log files, and generate an HTML report called output.html.

### 3. View the Report
Open output.html in a web browser to see the top words for each news category.

## Functionality

Here's an overview of what the script does:

### 1. Logging Configuration: 
The script sets up logging to record information about the processing steps. It logs both to the console and to individual log files for each category.

### 2. Tokenization and Word Counting: 
For each news category, the script tokenizes the headlines, filters out stopwords, punctuation, and short words, and counts the occurrences of each word.

### 3. HTML Report Generation: 
After processing all categories, the script generates an HTML report using the HtmlPage class. The report displays the top words for each category.
Customization

## Customization

You can customize the script by modifying the following:

- **data_file_path:** Change the path to your dataset file.
- **stopwords:** Customize the list of stopwords by editing the NLTK stopwords or adding your own.
- **top_words_count:** Modify the number of top words to display for each category.
- **log_file:** Change the name and location of the log files.
- **HtmlPage class:** Extend the HTML report generation functionality in the html_generator.py module to support additional HTML elements.

