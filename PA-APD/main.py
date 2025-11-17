from function import *
from petugas import *
from warga import *
from data import akun

def login():
    clear()
    print("=== LOGIN ===")
    username = input("Username : ").strip()
    password = input("Password : ").strip()

    if username in akun and akun[username]["password"] == password:
        print("Login berhasil!")
        delay()
        return username, akun[username]["role"]
    else:
        print("Username atau password salah!")
        delay()
        return None, None


def menu_petugas(username):
    while True:
        clear()
        print(f"=== MENU PETUGAS ({username}) ===")
        print("1. Lihat semua laporan")
        print("2. Ubah data laporan")
        print("3. Logout")

        pilihan = pilih_opsi("Pilih menu: ", ["1", "2", "3"])

        if pilihan == "1":
            clear()
            print("=== DAFTAR LAPORAN ===")
            print(tabel())
            input("\nEnter untuk kembali...")
        
        elif pilihan == "2":
            ubah_data_petugas()
            input("\nEnter untuk kembali...")

        elif pilihan == "3":
            return


def menu_warga(username):
    while True:
        clear()
        print(f"=== MENU WARGA ({username}) ===")
        print("1. Lihat laporan saya")
        print("2. Buat laporan baru")
        print("3. Logout")

        pilihan = pilih_opsi("Pilih menu: ", ["1", "2", "3"])

        if pilihan == "1":
            clear()
            lihat_laporan(username)
            input("\nEnter untuk kembali...")

        elif pilihan == "2":
            clear()
            buat_laporan(username)
            input("\nEnter untuk kembali...")

        elif pilihan == "3":
            return


def main():
    while True:
        clear()
        print("=== SISTEM LAPORAN ===")
        print("1. Login")
        print("2. Keluar")

        pilihan = pilih_opsi("Pilih menu: ", ["1", "2"])

        if pilihan == "1":
            username, role = login()
            if username:
                if role == "petugas":
                    menu_petugas(username)
                else:
                    menu_warga(username)

        elif pilihan == "2":
            clear()
            print("Keluar dari program...")
            delay()
            break


if __name__ == "__main__":
    main()


print(tabel())