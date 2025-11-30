import pandas as pd

# Membaca data mentah
def load_data(path="data/data.csv"):
    df = pd.read_csv(path)
    return df

# Membersihkan data sederhana
def clean_data(df):
    # Menghapus baris yang kosong
    df = df.dropna()
    return df

# Menyimpan data yang sudah dibersihkan
def save_clean_data(df, path="data/clean_data.csv"):
    df.to_csv(path, index=False)

# Program utama
if __name__ == "__main__":
    print("🔹 Membaca data...")
    raw = load_data(path='/content/dataset_retail_2014_2024.csv')

    print("🔹 Membersihkan data...")
    clean = clean_data(raw)

    print("🔹 Menyimpan data bersih...")
    save_clean_data(clean, path='project/data/clean_data.csv')

    print("✔ Data berhasil dibersihkan dan disimpan sebagai clean_data.csv")
