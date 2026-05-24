import pandas as pd
from utils.transform import transform

def test_transform_cleans_data():
    raw_data = {
        'Title': ['Produk A', 'Unknown Product', 'Produk C'], 
        'Price': ['$10.50', 'Price Unavailable', None], 
        'Rating': ['⭐ 4.5 / 5', 'Not Rated', 'Invalid Rating / 5'],
        'Total_Reviews': ['100 Reviews', '3 Colors', '10 Colors'],
        'Size': ['Size: L', 'None', 'M'],
        'Gender': ['Gender: Male', 'Female', 'Male']
    }
    df_raw = pd.DataFrame(raw_data)
    df_clean = transform(df_raw)
    
    # 1. Memastikan output DataFrame
    assert isinstance(df_clean, pd.DataFrame)
    
    # 2. Memastikan data kotor terbuang. Dari 3 data, harus sisa 1 (Produk A)
    assert len(df_clean) == 1
    
    # 3. Memastikan semua format sudah benar
    assert df_clean.iloc[0]['Title'] == 'Produk A'
    assert df_clean.iloc[0]['Price'] == 168000.0  # 10.50 * 16000
    assert df_clean.iloc[0]['Rating'] == 4.5
    assert df_clean.iloc[0]['Total_Reviews'] == 100.0
    assert isinstance(df_clean.iloc[0]['Size'], str)
    assert isinstance(df_clean.iloc[0]['Gender'], str)