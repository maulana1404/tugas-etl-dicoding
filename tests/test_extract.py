import pandas as pd
from unittest.mock import patch
from utils.extract import extract

def test_extract():
    # Membuat tiruan respons dari website agar tidak butuh internet saat test
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    html_content = '''
    <div class="collection-card">
        <h3 class="product-title">Baju Dicoding</h3>
        <div class="price-container"><span class="price">$15.0</span></div>
        <p>⭐ 4.0 / 5</p>
        <p>50 Reviews</p>
        <p>Size: L</p>
        <p>Gender: Male</p>
    </div>
    '''
    
    # Menggunakan "patch" bawaan asli Python agar tidak butuh library tambahan
    with patch('utils.extract.requests.get') as mock_get, \
         patch('utils.extract.time.sleep') as mock_sleep:
        
        # Memanipulasi request dan waktu jeda
        mock_get.return_value = MockResponse(html_content, 200)
        mock_sleep.return_value = None
        
        # Eksekusi fungsi
        df = extract("https://fashion-studio.dicoding.dev")
    
    # Validasi hasil
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.iloc[0]['Title'] == 'Baju Dicoding'
    assert len(df) == 50 # Karena looping 50 halaman