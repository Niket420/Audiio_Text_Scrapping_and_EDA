# Audiio_Text_Scrapping_and_EDA

## Web Scraping Using Selenium  

## Overview  
This project automates web scraping using **Selenium** (instead of BeautifulSoup) since the webpage loads content dynamically. The goal is to extract audio files and their corresponding text from a scrollable webpage.  

## Process  

### 1. Web Scraping  
- Used **Selenium** to automate Chrome and open the webpage.  
- Waited until the required **class (containing links)** was fully loaded.  
- Extracted unique links using a **set** data structure.  
- Visited each link, manually inspected the page to locate the **audio link**, and automated scraping.  

### 2. Data Preparation  
- Named each **audio file** appropriately.  
- Saved data in a **CSV file** with:  
  - **Site link** (source of text & audio).  
  - **Audio filename**.  
  - **Corresponding text**.  

## Setup Instructions  

### 1. Install Dependencies  
```bash
pip install selenium pandas
python3 webscrapping.py
