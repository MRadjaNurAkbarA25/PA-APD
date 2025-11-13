from data import *
from datetime import *

def lihat_laporan(pelapor):
    milik = {k: v for k, v in laporan.items() if v["pelapor"] == pelapor}
    if not milik:
        print("Belum ada laporan.")
        return
    for nomor, data in milik.items():
        print(f"\nLaporan #{nomor}")
        print(f"Pelapor: {data['pelapor']}")
        print(f"Keluhan: {data['keluhan']}")
        print(f"Status: {data['status']}")
        print(f"Respon: {data['respon']}")
        print(f"Tanggal: {data['date']}")
        print(f"Deskripsi: {desc.get(nomor, '-')}")

def buat_laporan(pelapor):
    nomor = str(len(laporan) + 1).zfill(4)
    keluhan = input("Keluhan (max 30 karakter): ")[:30]
    deskripsi = input("Deskripsi (max 100 karakter): ")[:100]
    laporan[nomor] = {
        "pelapor": pelapor,
        "keluhan": keluhan,
        "status": "diajukan",
        "respon": "",
        "date": datetime.now().strftime("%d/%m/%y %H:%M")
    }
    desc[nomor] = deskripsi
    print(f"Laporan #{nomor} berhasil dibuat!")
    
print('testdummy')