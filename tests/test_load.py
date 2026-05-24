import os
import pandas as pd
from utils.load import load

def test_load_saves_file():
    # 1. Membuat data bersih palsu (dummy data)
    dummy_data = pd.DataFrame({
        'Title': ['Kemeja Pria', 'Kaos Polos'],
        'Price': [15.5, 20.0],
        'Rating': [4.8, 5.0]
    })
    
    # 2. Menentukan nama file sementara khusus untuk testing
    test_filename = "data/test_output.csv"
    
    # 3. Memasukkan data ke mesin penyimpan (Load)
    load(dummy_data, target_file=test_filename)
    
    # 4. Mengecek apakah file test_output.csv benar-benar terbuat di laptop
    assert os.path.exists(test_filename), "Fungsi load gagal membuat file CSV"
    
    # 5. Mengecek apakah isi file yang tersimpan sesuai (tidak rusak)
    saved_df = pd.read_csv(test_filename)
    assert len(saved_df) == 2, "Jumlah baris data yang disimpan tidak sesuai"
    
    # 6. Menghapus file sementara tersebut agar folder tetap rapi
    if os.path.exists(test_filename):
        os.remove(test_filename)