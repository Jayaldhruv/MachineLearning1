#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Python script to scrape an article and save its text to a file
# Url: https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7

import os
import requests
from bs4 import BeautifulSoup
import re

def get_page():
    """
    Prompt the user for a Medium article URL and fetch its HTML content.
    """
    url = input("Enter the URL of a Medium article: ")

    # Validate URL format
    if not re.match(r'https?://medium.com/', url):
        print("Invalid URL. Please enter a valid Medium article URL.")
        exit(1)

    # Fetch page content
    response = requests.get(url)
    response.raise_for_status()
    return url, BeautifulSoup(response.text, 'html.parser')

def collect_text(soup, url):
    """
    Extract text content from the article and format it.
    """
    text = f"url: {url}\n\n"
    paragraphs = soup.find_all('p')  # Extract all paragraphs
    for para in paragraphs:
        text += f"{para.get_text(strip=True)}\n\n"  # Add each paragraph's text
    return text

def save_file(text, url):
    """
    Save the scraped text to a file in a directory.
    """
    # Create the directory if it doesn't exist
    os.makedirs('./scraped_articles', exist_ok=True)
    
    # Use the last part of the URL as the file name
    file_name = f"scraped_articles/{url.split('/')[-1]}.txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"File saved at: {file_name}")

if __name__ == '__main__':
    url, soup = get_page()
    text = collect_text(soup, url)
    save_file(text, url)
    # Run the script and provide the URL: 
    # https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7


# In[ ]:





# In[ ]:




