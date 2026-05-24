import pandas as pd
from unittest.mock import patch, MagicMock
from utils.load import load

@patch('utils.load.gspread.service_account')
@patch('pandas.DataFrame.to_csv')
@patch('os.makedirs')
def test_load_saves_file(mock_makedirs, mock_to_csv, mock_service_account):
    # 1. Setup Mocking
    df = pd.DataFrame({'Title': ['Produk A'], 'Price': [160000.0]})
    
    # Membuat objek mock yang berantai untuk gspread
    mock_gc = MagicMock()
    mock_sh = MagicMock()
    mock_worksheet = MagicMock()
    
    mock_service_account.return_value = mock_gc
    mock_gc.open_by_url.return_value = mock_sh
    mock_sh.sheet1 = mock_worksheet # Menghubungkan worksheet ke sheet1
    
    # 2. Eksekusi
    load(df, 'data/cleaned_data.csv', 'dummy_url')
    
    # 3. Validasi
    mock_to_csv.assert_called_once()
    mock_worksheet.clear.assert_called_once() # Sekarang pasti terdeteksi
    mock_worksheet.update.assert_called_once()