from function import *
from data import laporan, akun

def menu_ketua_rt(username):
    while True:
        clear()
        print(f'=== MENU KETUA RT ({username}) ===')
        print('1. Lihat Semua Laporan')
        print('2. Hapus Laporan')
        print('3. Lihat Statistik Status')
        print('4. Ekspor Laporan ke CSV')
        print('5. Lihat Daftar Akun')
        print('6. Buat Akun Baru')
        print('7. Ubah Role Akun')
        print('8. Hapus Akun')
        print('0. Logout')
        
        pilihan = pilih_opsi('Pilih: ', ['0','1','2','3','4','5','6','7','8'])

        if pilihan == '1':
            clear()
            from menu import tabel
            print(tabel())
            input('\nEnter untuk kembali...')

        elif pilihan == '2':
            nomor = input_str('Nomor laporan: ')
            if nomor not in laporan:
                print('Laporan tidak ditemukan')
                delay()
                continue
            konfirmasi = pilih_opsi('Hapus laporan? (y/n): ', ['y','n'])
            if konfirmasi == 'y':
                del laporan[nomor]
                print('Laporan dihapus')
            else:
                print('Dibatalkan')
            delay()

        elif pilihan == '3':
            clear()
            status_list = [data['status'] for data in laporan.values()]
            unique = set(status_list)
            print('=== STATISTIK LAPORAN ===')
            for status in sorted(unique):
                jumlah = status_list.count(status)
                print(f'{status}: {jumlah}')
            input('\nEnter untuk kembali...')

        elif pilihan == '4':
            import csv
            nama_file = input('Nama file (tanpa .csv): ').strip()
            if not nama_file:
                nama_file = 'laporan_rt'
            try:
                with open(f'{nama_file}.csv', 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['No', 'Pelapor', 'Keluhan', 'Deskripsi', 'Status', 'Respon', 'Waktu'])
                    for no, data in laporan.items():
                        writer.writerow([
                            no,
                            data['pelapor'],
                            data['keluhan'],
                            data['deskripsi'],
                            data['status'],
                            data['respon'],
                            data['date']
                        ])
                print(f'Laporan diekspor ke {nama_file}.csv')
            except Exception as e:
                print(f'Gagal: {e}')
            delay()

        elif pilihan == '5':
            clear()
            print('=== DAFTAR AKUN ===')
            print(f"{'Username':<15} {'Role':<12}")
            print("-" * 25)
            for user, info in akun.items():
                print(f"{user:<15} {info['role']:<12}")
            input('\nEnter untuk kembali...')

        elif pilihan == '6':
            user_baru = input_str('Username baru: ')
            if not user_baru.isalnum():
                print('Username hanya huruf/angka')
                delay()
                continue
            if user_baru in akun:
                print('Username sudah ada')
                delay()
                continue
            pw = input('Password (min 3): ').strip()
            if len(pw) < 3:
                print('Password minimal 3 karakter')
                delay()
                continue
            print('1. Warga\n2. Petugas')
            role_pilih = pilih_opsi('Pilih role: ', ['1','2'])
            role = 'warga' if role_pilih == '1' else 'petugas'
            akun[user_baru] = {'password': pw, 'role': role}
            print(f'Akun {user_baru} berhasil dibuat')
            delay()

        elif pilihan == '7':
            target = input_str('Username yang diubah: ')
            if target not in akun:
                print('Akun tidak ditemukan')
                delay()
                continue
            print('1. Warga\n2. Petugas\n3. Ketua RT')
            role_pilih = pilih_opsi('Role baru: ', ['1','2','3'])
            role_map = {'1': 'warga', '2': 'petugas', '3': 'ketua_rt'}
            akun[target]['role'] = role_map[role_pilih]
            print(f'Role {target} diubah')
            delay()

        elif pilihan == '8':
            target = input_str('Username yang dihapus: ')
            if target == username:
                print('Tidak bisa hapus diri sendiri')
                delay()
                continue
            if target not in akun:
                print('Akun tidak ditemukan')
                delay()
                continue
            konfirmasi = pilih_opsi(f'Hapus {target}? (y/n): ', ['y','n'])
            if konfirmasi == 'y':
                del akun[target]
                print(f'Akun {target} dihapus')
            else:
                print('Dibatalkan')
            delay()

        elif pilihan == '0':
            clear()
            return