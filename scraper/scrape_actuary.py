from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

# Setup Selenium
driver = webdriver.Chrome()
driver.get("https://www.actuarylist.com/")
time.sleep(5)

# Scroll to load all jobs
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Parse page content
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Extract job blocks
job_cards = soup.select("a.Job_job-page-link__a5I5g")
print(f"✅ Found {len(job_cards)} job cards")

jobs = []

for card in job_cards:
    job = {}
    
    # Job Title (inside <b>)
    title_tag = card.find("b")
    job["Title"] = title_tag.text.strip() if title_tag else ""
    
    # All <a> tags with location/tag class
    tag_links = card.select("a.Job_job-card__location__bq7jX")
    if tag_links:
        job["Location"] = tag_links[0].text.strip()
        job["Tags"] = ", ".join(a.text.strip() for a in tag_links[1:])  # Skip location
    else:
        job["Location"] = ""
        job["Tags"] = ""

    # Company Name from <p> tag
    company_tag = card.find("p")
    job["Company"] = company_tag.text.strip() if company_tag else ""

    # Job URL
    job["Link"] = "https://www.actuarylist.com" + card.get("href", "")
    
    jobs.append(job)

# Save to CSV
with open("full_actuary_jobs.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Title", "Company", "Location", "Tags", "Link"])
    writer.writeheader()
    writer.writerows(jobs)

print("✅ Job data saved to full_actuary_jobs.csv")
