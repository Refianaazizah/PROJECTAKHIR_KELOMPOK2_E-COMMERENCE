produk = {
    "001": {"nama": "Laptop", "harga": 10000000},
    "002": {"nama": "Smartphone", "harga": 5000000},
    "003": {"nama": "Headphone", "harga": 1500000},
    "004": {"nama": "Printer", "harga": 3000000},
}

pengguna = {
    "user1": "password1",
    "user2": "password2",
    "admin": "admin123"
}

def tampilkan_produk():
    print("\nDaftar Produk:")
    for kode, info in produk.items():
        print(f"{kode}: {info['nama']} - Rp {info['harga']:,}")

def hitung_total_harga(kode_produk, jumlah):
    harga = produk[kode_produk]["harga"]
    total = harga * jumlah
    return total

def konfirmasi_pesanan(kode_produk, jumlah):
    total_harga = hitung_total_harga(kode_produk, jumlah)
    print(f"\nAnda memesan {jumlah} {produk[kode_produk]['nama']}.")
    print(f"Total harga: Rp {total_harga:,}")
    konfirmasi = input("Apakah Anda ingin melanjutkan pesanan? (ya/tidak): ").strip()
    return konfirmasi == "ya" or konfirmasi == "Ya"


def login():
    print("=== Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in pengguna and pengguna[username] == password:
        print("Login berhasil!")
        return True
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return False

def main():
    while not login():
        continue  

    while True:
        tampilkan_produk()
        
        kode_produk = input("\nMasukkan kode produk yang ingin dipesan (atau ketik 'keluar' untuk selesai): ").strip()
        
        if kode_produk == 'keluar' or kode_produk == 'Keluar':
            print("Terima kasih telah berbelanja!")
            break
        
        if kode_produk not in produk:
            print("Kode produk tidak valid. Silakan coba lagi.")
            continue
        
        try:
            jumlah = int(input("Masukkan jumlah yang ingin dipesan: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue
        
        if konfirmasi_pesanan(kode_produk, jumlah):
            print("Pesanan Anda telah dikonfirmasi!")
        else:
            print("Pesanan dibatalkan.")

main()