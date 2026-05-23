from utils.extract import extract
from utils.transform import transform
from utils.load import load

def run_pipeline():
    url = "https://fashion-studio.dicoding.dev/"
    
    print("=== Memulai ETL Pipeline ===")
    
    # 1. Fase Extract
    print("\n[1/3] Mengambil data dari website (Extract)...")
    df_raw = extract(url)
    print(f"Berhasil mengambil {len(df_raw)} data produk.")
    
    # 2. Fase Transform
    print("\n[2/3] Membersihkan data (Transform)...")
    df_clean = transform(df_raw)
    print(f"Data setelah dibersihkan tersisa {len(df_clean)} produk.")
    
    # 3. Fase Load
    print("\n[3/3] Menyimpan data (Load)...")
    load(df_clean, target_file="data/cleaned_data.csv")
    
    print("\n=== ETL Pipeline Selesai Sukses! ===")

if __name__ == "__main__":
    run_pipeline()