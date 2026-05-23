import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(url):
    # 1. Meminta izin mengambil data dari website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 2. Mencari semua kartu produk (berdasarkan gambar petunjuk Dicoding)
    cards = soup.find_all('div', class_='collection-card')
    
    data = []
    
    # 3. Mulai mengambil elemen dari masing-masing kartu
    for card in cards:
        # Ambil Judul
        title_tag = card.find('h3', class_='product-title')
        title = title_tag.text.strip() if title_tag else None
        
        # Ambil Harga (Harus menangani 2 kondisi tag HTML berbeda sesuai Tips & Trik)
        price = None
        price_container = card.find('div', class_='price-container')
        if price_container:
            price_span = price_container.find('span', class_='price')
            if price_span:
                price = price_span.text.strip()
        else:
            price_p = card.find('p', class_='price')
            if price_p:
                price = price_p.text.strip()
                
        # Ambil Rating, Reviews, Size, dan Gender (Biasanya ada di dalam tag <p>)
        rating = None
        reviews = None
        size = None
        gender = None
        
        p_tags = card.find_all('p')
        for p in p_tags:
            text = p.text.strip()
            if text.startswith('⭐'):
                rating = text
            elif 'Colors' in text or 'Reviews' in text:
                reviews = text
            elif text.startswith('Size:'):
                size = text
            elif text.startswith('Gender:'):
                gender = text
        
        # Simpan ke dalam list
        data.append({
            'Title': title,
            'Price': price,
            'Rating': rating,
            'Total_Reviews': reviews,
            'Size': size,
            'Gender': gender
        })
        
    # 4. Ubah menjadi Pandas DataFrame agar mudah diolah nanti
    return pd.DataFrame(data)

# Blok ini hanya untuk menguji apakah kodenya berhasil jalan
if __name__ == "__main__":
    url = "https://fashion-studio.dicoding.dev/"
    df = extract(url)
    print("=== Data Berhasil Diambil ===")
    print(df.head())
    print(f"\nTotal data: {len(df)} produk")