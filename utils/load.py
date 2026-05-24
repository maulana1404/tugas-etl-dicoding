import os
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

def load(df, target_file="data/cleaned_data.csv", spreadsheet_url=None):
    # 1. Simpan sebagai file CSV lokal (sesuai kriteria wajib)
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    df.to_csv(target_file, index=False)
    print(f"✅ Data berhasil disimpan secara lokal ke {target_file}")

    # 2. Kirim ke Google Sheets (jika URL diberikan)
    if spreadsheet_url:
        print("Menghubungkan ke Google Sheets...")
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        
        try:
            # Membaca kunci rahasia
            credentials = Credentials.from_service_account_file('google-sheets-api.json', scopes=scopes)
            gc = gspread.authorize(credentials)
            
            # Membuka spreadsheet dan worksheet pertama
            sheet = gc.open_by_url(spreadsheet_url)
            worksheet = sheet.get_worksheet(0)
            
            # Membersihkan isi lama dan memasukkan data baru
            worksheet.clear()
            df = df.fillna("")
            data_to_upload = [df.columns.values.tolist()] + df.values.tolist()
            worksheet.update(values=data_to_upload, range_name='A1')
            
            print("☁️ Yeay! Data berhasil diunggah ke Google Sheets!")
            
        except Exception as e:
            print(f"❌ Gagal mengunggah ke Google Sheets: {e}")


    worksheet.clear()
    
    # TAMBAHKAN BARIS INI: Mengubah sisa NaN (jika ada) menjadi teks kosong
    df = df.fillna("")
    
    data_to_upload = [df.columns.values.tolist()] + df.values.tolist()
    worksheet.update(values=data_to_upload, range_name='A1')