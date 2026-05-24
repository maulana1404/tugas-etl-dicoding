import pandas as pd
from utils.transform import transform
def test_transform_cleans_data():
    # 1. Membuat data kotor palsu (dummy data)
    dummy_data = pd.DataFrame({
        'Title': ['Kemeja Pria', 'Kaos Polos', None],
        'Price': ['$15.5', 'Rp 20.0', '$30.0'],
        'Rating': ['⭐ 4.8', '5.0 ⭐', '3.5'],
        'Size': ['Size: M', 'L', 'Size: XL']
    })
    # 2. Memasukkan data kotor ke mesin pembersih
    cleaned_df = transform(dummy_data)
    # 3. Mengecek penghapusan baris kosong
    assert len(cleaned_df) == 2, "Baris yang Title-nya kosong gagal dihapus"
    # 4. Mengecek pembersihan Harga (Price)
    assert cleaned_df['Price'].iloc[0] == 15.5, "Harga gagal dibersihkan menjadi angka murni"
    # 5. Mengecek pembersihan Rating
    assert cleaned_df['Rating'].iloc[0] == 4.8, "Rating gagal dibersihkan dari simbol bintang"
    # 6. Mengecek pembersihan Ukuran (Size)
    assert cleaned_df['Size'].iloc[0] == 'M', "Teks 'Size:' gagal dihapus"