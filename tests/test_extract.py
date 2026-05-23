import pandas as pd
from utils.extract import extract

def test_extract_returns_dataframe():
    """
    Skenario Tes: Memastikan fungsi extract berjalan dengan benar
    dan mengembalikan data dalam format Pandas DataFrame yang tidak kosong.
    """
    url = "https://fashion-studio.dicoding.dev/"
    df = extract(url)
    
    # 1. Mengecek apakah hasilnya benar-benar sebuah DataFrame
    assert isinstance(df, pd.DataFrame), "Hasil extract harus berupa Pandas DataFrame"
    
    # 2. Mengecek apakah datanya ada (tidak kosong / panjangnya lebih dari 0)
    assert len(df) > 0, "Data yang diekstrak tidak boleh kosong"
    
    # 3. Mengecek apakah kolom-kolom utama berhasil terambil
    expected_columns = ['Title', 'Price', 'Rating']
    for col in expected_columns:
        assert col in df.columns, f"Kolom {col} tidak ditemukan dalam data hasil extract"