import pandas as pd
import numpy as np

def transform(df):
    df_clean = df.copy()

    # 1. Hapus duplikat
    df_clean = df_clean.drop_duplicates()

    # 2. TANGANI DIRTY PATTERNS DARI REVIEWER
    # Filter Kolom Title
    if 'Title' in df_clean.columns:
        df_clean['Title'] = df_clean['Title'].replace(["Unknown Product"], np.nan)

    # Filter Kolom Price dan Konversi ke Rupiah
    if 'Price' in df_clean.columns:
        df_clean['Price'] = df_clean['Price'].replace(["Price Unavailable", None], np.nan)
        # Ambil angkanya saja, pastikan tipe data numerik, lalu kali 16000
        df_clean['Price'] = df_clean['Price'].astype(str).str.extract(r'([\d.]+)')[0]
        df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce') * 16000

    # Filter Kolom Rating (Harus Float)
    if 'Rating' in df_clean.columns:
        df_clean['Rating'] = df_clean['Rating'].replace(["Invalid Rating / 5", "Not Rated", "Invalid Rating"], np.nan)
        # Ambil angkanya saja untuk membuang teks " / 5"
        df_clean['Rating'] = df_clean['Rating'].astype(str).str.extract(r'([\d.]+)')[0]
        df_clean['Rating'] = pd.to_numeric(df_clean['Rating'], errors='coerce')

    # Filter Kolom Total_Reviews / Colors (Harus Angka)
    if 'Total_Reviews' in df_clean.columns:
        # Mengambil angka saja dari "3 Colors" atau "10 Reviews"
        df_clean['Total_Reviews'] = df_clean['Total_Reviews'].astype(str).str.extract(r'(\d+)')[0]
        df_clean['Total_Reviews'] = pd.to_numeric(df_clean['Total_Reviews'], errors='coerce')

    # Filter Kolom Size dan Gender (Teks Bersih)
    if 'Size' in df_clean.columns:
        df_clean['Size'] = df_clean['Size'].astype(str).str.replace('Size:', '', case=False).str.strip()
        df_clean['Size'] = df_clean['Size'].replace(['None', 'nan', ''], np.nan)

    if 'Gender' in df_clean.columns:
        df_clean['Gender'] = df_clean['Gender'].astype(str).str.replace('Gender:', '', case=False).str.strip()
        df_clean['Gender'] = df_clean['Gender'].replace(['None', 'nan', ''], np.nan)

    # 3. BUANG SEMUA DATA INVALID
    # dropna() akan otomatis menghapus baris yang tadi kita ubah menjadi NaN
    df_clean = df_clean.dropna()

    # 4. Syarat Wajib: Size dan Gender harus berisikan string
    if 'Size' in df_clean.columns:
        df_clean['Size'] = df_clean['Size'].astype(str)
    if 'Gender' in df_clean.columns:
        df_clean['Gender'] = df_clean['Gender'].astype(str)

    return df_clean