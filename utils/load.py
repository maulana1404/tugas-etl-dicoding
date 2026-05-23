import os
import pandas as pd

def load(df, target_file="data/cleaned_data.csv"):
    # Mengambil nama folder dari target_file (yaitu folder 'data')
    folder_name = os.path.dirname(target_file)
    
    # Membuat folder 'data' secara otomatis jika belum ada
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    # Menyimpan DataFrame ke format CSV tanpa menyertakan nomor index
    df.to_csv(target_file, index=False)
    
    print(f"Data berhasil disimpan dengan aman di: {target_file}")