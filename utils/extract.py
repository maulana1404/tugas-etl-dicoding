import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def extract(base_url):
    data = []
    print("Memulai proses scraping 50 halaman...")
    
    # Memastikan tidak ada garis miring ganda di URL
    clean_base = base_url.rstrip('/') 
    
    for page in range(1, 51):
        # JEBAKAN TERPECAHKAN: Format pagination yang benar!
        if page == 1:
            url = f"{clean_base}/"
        else:
            url = f"{clean_base}/page{page}/"
            
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', class_='collection-card')
        
        for card in cards:
            title_tag = card.find('h3', class_='product-title')
            title = title_tag.text.strip() if title_tag else None
            
            price = None
            price_container = card.find('div', class_='price-container')
            if price_container:
                price_span = price_container.find('span', class_='price')
                if price_span: price = price_span.text.strip()
            else:
                price_p = card.find('p', class_='price')
                if price_p: price = price_p.text.strip()
            
            rating = None
            reviews = None
            size = None
            gender = None
            
            # Pengecekan teks yang JAUH lebih kebal error menggunakan 'in'
            for p in card.find_all('p'):
                text = p.text.strip()
                if '⭐' in text or 'Invalid' in text:
                    rating = text
                elif 'Review' in text or 'Color' in text:
                    reviews = text
                elif 'Size' in text or 'size' in text.lower():
                    size = text
                elif 'Gender' in text or 'gender' in text.lower():
                    gender = text
            
            data.append({
                'Title': title,
                'Price': price,
                'Rating': rating,
                'Total_Reviews': reviews,
                'Size': size,
                'Gender': gender
            })
            
        time.sleep(1)
        
    return pd.DataFrame(data)