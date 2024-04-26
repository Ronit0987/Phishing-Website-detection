from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd
# List of URLs to scrape
df=pd.read_csv("F:\edge_downloads\phishing_urls.csv")
df=df[51:100]

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Create a directory to save DOM tree files
if not os.path.exists('dom_trees'):
    os.makedirs('dom_trees')

# Loop through each URL
for url in urls:
    # Open the URL
    driver.get(url)

    # Get the DOM tree
    dom_tree = driver.page_source

    # Save the DOM tree to a file
    filename = f"dom_trees/{url.replace('https://', '').replace('http://', '')}_dom_tree.html"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(dom_tree)

    print(f"DOM tree saved for {url} as {filename}")

# Quit the WebDriver
driver.quit()
