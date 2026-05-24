import gspread
import pandas as pd
import os

def load(df, target_file, spreadsheet_url):
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    df.to_csv(target_file, index=False)
    print(f"Data bersih disimpan di {target_file}")

    try:
        gc = gspread.service_account(filename='google-sheets-api.json')
        sh = gc.open_by_url(spreadsheet_url)
        worksheet = sh.sheet1
        
        worksheet.clear()
        df = df.fillna("")
        data_to_upload = [df.columns.values.tolist()] + df.values.tolist()
        worksheet.update(values=data_to_upload, range_name='A1')
        print("Data berhasil diunggah ke Google Sheets")
    except Exception as e:
        print(f"Proses unggah gagal, menghentikan eksekusi sheet. Error: {e}")