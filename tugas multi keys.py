import datetime
import os

# Data awal perpustakaan (Nesting Dictionary dengan Multi-Keys)
data_buku = {
    'BK001': {
        'judul': 'kejeniusan ompik',
        'penulis': 'mbah basuki',
        'tahun': 2026,
        'tgl_pinjam': datetime.date(2026, 11, 15),
        'status': 'TIDAK'
    },
    'BK002': {
        'judul': 'Bumi',
        'penulis': 'Tere Liye',
        'tahun': 2014,
        'tgl_pinjam': datetime.date(2026, 11, 1),
        'status': 'TERSEDIA'
    }
}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("="*85)
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^85}")
    print("="*85)
    
    # Menampilkan Data Buku (Format rapi dengan f-string)
    print(f"{'KEYS':<8} | {'JUDUL BUKU':<22} | {'PENULIS':<18} | {'TAHUN':<6} | {'TGL PINJAM':<12} | {'STATUS':<10}")
    print("-"*85)
    
    for key in data_buku:
        KEY = key
        JUDUL = data_buku[KEY]['judul']
        PENULIS = data_buku[KEY]['penulis']
        TAHUN = data_buku[KEY]['tahun']
        TGL_PINJAM = data_buku[KEY]['tgl_pinjam'].strftime("%d-%m-%Y")
        STATUS = data_buku[KEY]['status']
        
        print(f"{KEY:<8} | {JUDUL:<22} | {PENULIS:<18} | {TAHUN:<6} | {TGL_PINJAM:<12} | {STATUS:<10}")
    
    print("="*85)
    
    # Menu Tambah Buku Baru
    pilihan = input("\nApakah ingin menambah buku baru? (y/n): ").lower()
    if pilihan == 'n':
        break
    elif pilihan == 'y':
        print("\n--- INPUT BUKU BARU ---")
        key_baru = input("Masukkan KEY Baru (Contoh: BK004): ").upper()
        judul_baru = input("Masukkan Judul Buku: ")
        penulis_baru = input("Masukkan Nama Penulis: ")
        tahun_baru = int(input("Masukkan Tahun Terbit: "))
        
        # Tanggal default saat diinput
        tgl_sekarang = datetime.date.today()
        status_baru = input("Masukkan Status (TERSEDIA / TIDAK): ").upper()
        
        # Menambahkan data baru ke dalam nesting dictionary
        data_buku[key_baru] = {
            'judul': judul_baru,
            'penulis': penulis_baru,
            'tahun': tahun_baru,
            'tgl_pinjam': tgl_sekarang,
            'status': status_baru if status_baru in ['TERSEDIA', 'TIDAK'] else 'TERSEDIA'
        }
        print("\n[Berhasil] Buku baru telah ditambahkan ke sistem!")
        input("\nTekan Enter untuk melanjutkan...")

print("\nAkhir dari program, terima kasih.")