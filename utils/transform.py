import pandas as pd

def transform(df):
    # Membuat copy data agar data aslinya tetap aman
    df_clean = df.copy()

    # 1. Membersihkan kolom Price 
    # Menghapus simbol mata uang dan huruf, menyisakan angka dan titik, lalu mengubahnya jadi float
    if 'Price' in df_clean.columns:
        df_clean['Price'] = df_clean['Price'].astype(str).str.replace(r'[^\d.]', '', regex=True)
        df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce')

    # 2. Membersihkan kolom Rating 
    # Menghapus simbol bintang (⭐) dan mengubahnya jadi tipe data angka
    if 'Rating' in df_clean.columns:
        df_clean['Rating'] = df_clean['Rating'].astype(str).str.replace(r'[^\d.]', '', regex=True)
        df_clean['Rating'] = pd.to_numeric(df_clean['Rating'], errors='coerce')

    # 3. Membersihkan kolom Total_Reviews
    # Mengambil angkanya saja
    if 'Total_Reviews' in df_clean.columns:
        df_clean['Total_Reviews'] = df_clean['Total_Reviews'].astype(str).str.replace(r'[^\d]', '', regex=True)
        df_clean['Total_Reviews'] = pd.to_numeric(df_clean['Total_Reviews'], errors='coerce')

    # 4. Membersihkan teks awalan pada kolom Size dan Gender
    if 'Size' in df_clean.columns:
        df_clean['Size'] = df_clean['Size'].astype(str).str.replace('Size:', '', case=False).str.strip()

    if 'Gender' in df_clean.columns:
        df_clean['Gender'] = df_clean['Gender'].astype(str).str.replace('Gender:', '', case=False).str.strip()

    # 5. Menghapus baris yang datanya kosong (corrupt) pada bagian Title atau Price
    df_clean = df_clean.dropna(subset=['Title', 'Price'])

    return df_clean

# Blok ini hanya untuk menguji apakah kodenya berhasil jalan
if __name__ == "__main__":
    from extract import extract
    
    url = "https://fashion-studio.dicoding.dev/"
    print("1. Mengambil data mentah...")
    df_raw = extract(url)
    
    print("2. Memulai proses pembersihan data...")
    df_clean = transform(df_raw)
    
    print("\n=== Data Setelah Dibersihkan ===")
    print(df_clean[['Title', 'Price', 'Rating', 'Size']].head())
    print(f"\nTotal data bersih: {len(df_clean)} produk")