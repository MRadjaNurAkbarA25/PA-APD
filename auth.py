from function import *
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


def register():
    print("===Daftar Akun===")
    username = input("Masukkan Username: ").strip()
    password = input ("Masukkan Password: ").strip()
    if username in akun:
        print("username sudah digunakan!")
        return
    else:
        akun[username] = {"password": password, "role": "warga"}
        print ("akun berhasil di daftarkan silakan login")
        return