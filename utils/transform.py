import pandas as pd
import numpy as np

def transform(df):
    df_clean = df.copy()

    # 1. Hapus Duplikat
    df_clean = df_clean.drop_duplicates()

    # 2. Bersihkan Price
    if 'Price' in df_clean.columns:
        df_clean['Price'] = df_clean['Price'].astype(str).str.extract(r'([\d.]+)')[0]
        df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce') * 16000

    # 3. Bersihkan Rating
    if 'Rating' in df_clean.columns:
        df_clean['Rating'] = df_clean['Rating'].replace('Invalid Rating', np.nan)
        df_clean['Rating'] = df_clean['Rating'].astype(str).str.extract(r'([\d.]+)')[0]
        df_clean['Rating'] = pd.to_numeric(df_clean['Rating'], errors='coerce')

    # 4. Bersihkan Total_Reviews
    if 'Total_Reviews' in df_clean.columns:
        df_clean['Total_Reviews'] = df_clean['Total_Reviews'].astype(str).str.extract(r'(\d+)')[0]
        df_clean['Total_Reviews'] = pd.to_numeric(df_clean['Total_Reviews'], errors='coerce')

    # 5. Bersihkan Size dan Gender
    if 'Size' in df_clean.columns:
        df_clean['Size'] = df_clean['Size'].astype(str).str.replace('Size:', '', case=False).str.strip()
        df_clean['Size'] = df_clean['Size'].replace(['None', 'nan', ''], np.nan)

    if 'Gender' in df_clean.columns:
        df_clean['Gender'] = df_clean['Gender'].astype(str).str.replace('Gender:', '', case=False).str.strip()
        df_clean['Gender'] = df_clean['Gender'].replace(['None', 'nan', ''], np.nan)

    # 6. MENGHAPUS SEMUA BARIS KOSONG
    df_clean = df_clean.dropna()
    
    return df_clean