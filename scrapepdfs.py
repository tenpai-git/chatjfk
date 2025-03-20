import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_URL = "https://www.archives.gov/research/jfk/release-2025?page="
SAVE_DIR = "jfk_pdfs"
os.makedirs(SAVE_DIR, exist_ok=True)

def get_pdf_links(page_num):
    url = BASE_URL + str(page_num)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    pdf_links = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.endswith(".pdf"):
            pdf_links.append("https://www.archives.gov" + href)
    return pdf_links

def download_pdf(pdf_url):
    pdf_name = os.path.join(SAVE_DIR, pdf_url.split("/")[-1])
    response = requests.get(pdf_url, stream=True)
    with open(pdf_name, "wb") as f:
        for chunk in tqdm(response.iter_content(1024), desc=f"Downloading {pdf_name}"):
            f.write(chunk)

for page in range(1, 220):  # Pages 1 to 219
    pdf_links = get_pdf_links(page)
    for pdf in pdf_links:
        download_pdf(pdf)

