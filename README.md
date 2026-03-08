# AI Sentiment Analysis Tool

A Python-based Natural Language Processing (NLP) project that evaluates the emotional tone of text. This project includes two specialized tools: one for analyzing local text files and another for extracting and analyzing live news articles from the web.

🚀 Features
Web Scraping Integration: Uses the newspaper3k library to fetch, parse, and summarize online articles automatically.

Local File Processing: Capability to read and analyze .txt files for batch sentiment processing.

NLP Analysis: Leverages TextBlob to calculate sentiment polarity on a scale of -1 (negative) to 1 (positive).

Automated Summarization: Utilizes Natural Language Processing to extract key summaries from long-form web content before analysis.

🛠️ Tech Stack
Language: Python

NLP Library: TextBlob

Web Scraper: Newspaper3k

Environment: Python 3.x

📂 Project Structure
textAnalysis.py: Script for analyzing sentiment from local text files (myText.txt).

urlAnalysis.py: Script for extracting and analyzing sentiment from a provided URL.

myText.txt: Sample input file for local analysis.
