import pandas as pd

# Membaca dataset dari file CSV dengan encoding dan menghilangkan spasi tersembunyi
file_path = r"D:\TUGAS PAA 2\tugas1PAA2\dataset_harga_bunga.csv"
df = pd.read_csv(file_path, encoding="utf-8")

# Membersihkan nama kolom dari spasi tersembunyi
df.columns = df.columns.str.strip()

# Menampilkan nama kolom untuk memastikan tidak ada typo
print("Nama kolom dalam dataset:", df.columns)

# Mengambil data harga produk dalam bentuk list, jika kolom tersedia
column_name = "Harga Produk (Ribu Rupiah)"
if column_name in df.columns:
    data = df[column_name].tolist()
else:
    print(f"Error: Kolom '{column_name}' tidak ditemukan dalam dataset.")
    data = []

# Fungsi Selection Sort dengan menampilkan proses pertukaran
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(f"Tukar {arr[min_index]} dengan {arr[i]}: {arr}")

# Menjalankan Selection Sort jika data tidak kosong
if data:
    print("Proses Sorting:")
    selection_sort(data)
    print("\nHarga Bunga setelah diurutkan (dari termurah ke termahal):")
    print(data)
else:
    print("Sorting tidak dapat dilakukan karena data kosong.")