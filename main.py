from function import *
from petugas import *
from warga import *
from data import akun


def register():
    clear()
    print("=== DAFTAR AKUN BARU ===")
    username = input("Buat username : ").strip()

    if username in akun:
        print("Username sudah dipakai!")
        delay()
        return

    password = input("Buat password : ").strip()

    # Pilih role
    print("\nPilih jenis akun:")
    print("1. Warga")
    print("2. Petugas")
    role = pilih_opsi("Role: ", ["1", "2"])

    role = "warga" if role == "1" else "petugas"

    akun[username] = {
        "password": password,
        "role": role
    }

    print("\nAkun berhasil dibuat!")
    delay()


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
            break


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
            lihat_laporan_spesifik(username)
            input("\nEnter untuk kembali...")

        elif pilihan == "2":
            clear()
            buat_laporan(username)
            input("\nEnter untuk kembali...")

        elif pilihan == "3":
            break


def main():
    user_login = None  # menyimpan username jika sedang login

    while True:
        clear()
        print("=== SISTEM LAPORAN ===")
        print("1. Login")
        print("2. Register")
        print("3. Logout")
        print("4. Keluar")

        pilihan = pilih_opsi("Pilih menu: ", ["1", "2", "3", "4"])

        # LOGIN
        if pilihan == "1":
            if user_login:
                print("Anda sudah login!")
                delay()
            else:
                username, role = login()
                if username:
                    user_login = (username, role)
                    if role == "petugas":
                        menu_petugas(username)
                    else:
                        menu_warga(username)
                    user_login = None  # logout otomatis saat keluar menu

        # REGISTER
        elif pilihan == "2":
            register()

        # MANUAL LOGOUT
        elif pilihan == "3":
            if user_login:
                print("Berhasil logout.")
                user_login = None
            else:
                print("Anda belum login.")
            delay()

        # KELUAR PROGRAM
        elif pilihan == "4":
            clear()
            print("Menutup program...")
            delay()
            break


if __name__ == "__main__":
    main()
