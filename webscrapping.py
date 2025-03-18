import time
import os
import requests
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver options
options = Options()
options.headless = False  # Keep browser visible
service = Service(ChromeDriverManager().install())  # Auto-install ChromeDriver
driver = webdriver.Chrome(service=service, options=options)

audio_folder = 'downloaded_audios'
csv_file = "scraped_data.csv"
extracted_links = set()


def download_audio(audio_url, file_name):
    os.makedirs(audio_folder, exist_ok=True)
    if not audio_url:
        return None

    file_path = os.path.join(audio_folder, file_name)
    response = requests.get(audio_url)

    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        return file_name
    return None


def save_to_csv(site_link, audio_file, text):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["site_link", "audio", "text"])
        writer.writerow([site_link, audio_file, text])


def scrapping_audio_text(url_to_site):
    driver.get(url_to_site)
    time.sleep(5)

    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'audio-player'))
    # )
    try:
        audio = driver.find_element(By.CLASS_NAME, 'audio-player')
        href = audio.get_attribute('src')
    except:
        href = None

    try:
        text_container = driver.find_element(By.CSS_SELECTOR, '.chapter.justify')
        text = text_container.text
    except:
        text = None

    return href if href else None, text if text else None


def scroll_and_extract_links(scrollable_box):
    last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_box)
    scroll_pause_time = 2

    while True:
        # Extract links before scrolling
        containers = scrollable_box.find_elements(By.TAG_NAME, 'a')

        for link in containers:
            href = link.get_attribute('href')
            if href and href not in extracted_links:
                extracted_links.add(href)
                print(href)  # Print new link found

        # Scroll down using scrollTop instead of scrollBy
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_box)
        time.sleep(scroll_pause_time)

        # Check for new height after scrolling
        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_box)
        if new_height == last_height:
            print("No more new content to load.")
            break
        last_height = new_height


def scrape_links_to_different_pages(url):
    driver.get(url)
    time.sleep(5)  # Allow initial load

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[role="main"].recordings-database div.default-width-container.db-container'))
        )

        scrollable_box = driver.find_element(By.CSS_SELECTOR,
                                             'div[role="main"].recordings-database div.default-width-container.db-container')
        scroll_and_extract_links(scrollable_box)

    except Exception as e:
        print("Error during scraping:", e)


if __name__ == "__main__":
    scrape_links_to_different_pages("https://www.faithcomesbyhearing.com/audio-bible-resources/recordings-database")

    for link in extracted_links:
        audio, text = scrapping_audio_text(link)
        if audio and text:
            audio_file = download_audio(audio, f"audio_{hash(link)}.mp3")
            save_to_csv(link, audio_file, text)

    driver.quit()