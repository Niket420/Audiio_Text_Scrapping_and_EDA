
# Audiio Text Scraping and EDA

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Selenium-WebScraping-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Pandas-DataProcessing-orange?style=flat-square"/>
</p>




## Overview

This project focuses on web scraping dynamic content using Selenium.
It extracts audio files and their corresponding text from a scrollable webpage where static scraping tools are not sufficient.


## Workflow

### 1. Web Scraping
	•	Automated browser interaction using Selenium (Chrome)
	•	Waited for dynamically loaded elements to appear
	•	Extracted unique links using a set
	•	Navigated to each link to:
	•	locate audio source
	•	extract corresponding text


### 2. Data Preparation
	•	Assigned meaningful filenames to audio files
	•	Stored results in a structured CSV file with:
	•	source link
	•	audio filename
	•	extracted text


## Project Structure

.
├── webscrapping.py
├── data/
│   ├── audio_files/
│   └── dataset.csv
└── README.md



Setup

Install Dependencies

pip install selenium pandas




Run Script

python3 webscrapping.py




Output
	•	Audio files saved locally
	•	CSV file containing:
	•	source link
	•	audio file name
	•	corresponding text



## Key Notes
	•	Selenium is used due to dynamic content loading
	•	Requires ChromeDriver compatible with your browser version
	•	Ensure proper waiting strategies to avoid missing elements



## Future Improvements
	•	Add headless browser support
	•	Improve scraping speed with parallel processing
	•	Automate driver setup
	•	Add error handling and retries
