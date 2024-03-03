# Achmad Rizqy Pranata - 2209116086
# Program CRUD Pembelian Game Digital (Steam) menggunakan Struktur Data Linked List (Single)

class Node:
    def __init__(self, id_game, judul, genre, harga, tipe):
        self.id_game = id_game
        self.judul = judul
        self.genre = genre
        self.harga = harga
        self.tipe = tipe
        self.next = None

class GameSteam:
    def __init__(self):
        self.head = None

    def tambah_game_awal(self, id_game, judul, genre, harga, tipe):
        new_node = Node(id_game, judul, genre, harga, tipe)
        new_node.next = self.head
        self.head = new_node
        print("Game berhasil ditambahkan ke Steam.")

    def tambah_game_akhir(self, id_game, judul, genre, harga, tipe):
        new_node = Node(id_game, judul, genre, harga, tipe)
        if self.head is None:
            self.head = new_node
            print("Game berhasil ditambahkan ke Steam.")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        print("Game berhasil ditambahkan ke Steam.")

    def tambah_game_di_antara(self, id_game_sebelum, id_game_baru, judul, genre, harga, tipe):
        new_node = Node(id_game_baru, judul, genre, harga, tipe)
        temp = self.head
        while temp:
            if temp.id_game == id_game_sebelum:
                new_node.next = temp.next
                temp.next = new_node
                print("Game berhasil ditambahkan ke Steam.")
                return
            temp = temp.next
        print(f"Game dengan ID {id_game_sebelum} tidak ditemukan.")

    def tampilkan_game(self):
        temp = self.head
        if temp is None:
            print("Steam belum memiliki game atau DLC.")
        else:
            print("Daftar Game dan DLC di Steam:")
            while temp:
                print(f"ID: {temp.id_game}, Judul: {temp.judul}, Genre: {temp.genre}, Harga: {temp.harga}, Tipe: {temp.tipe}")
                temp = temp.next

    def perbarui_game(self, id_game, judul=None, genre=None, harga=None, tipe=None):
        temp = self.head
        while temp is not None:
            if temp.id_game == id_game:
                if judul:
                    temp.judul = judul
                if genre:
                    temp.genre = genre
                if harga:
                    temp.harga = harga
                if tipe:
                    temp.tipe = tipe
                print("Data game atau DLC berhasil diperbarui.")
                return
            temp = temp.next
        print("ID game tidak ditemukan.")

    def hapus_game_awal(self):
        if self.head is None:
            print("Steam belum memiliki game atau DLC.")
            return

        self.head = self.head.next
        print("Game atau DLC pertama berhasil dihapus dari Steam.")

    def hapus_game_akhir(self):
        if self.head is None:
            print("Steam belum memiliki game atau DLC.")
            return

        temp = self.head
        if temp.next is None:
            self.head = None
            print("Game atau DLC terakhir berhasil dihapus dari Steam.")
            return

        while temp.next.next:
            temp = temp.next

        temp.next = None
        print("Game atau DLC terakhir berhasil dihapus dari Steam.")

    def hapus_game_di_antara(self, id_game_sebelum):
        if self.head is None:
            print("Steam belum memiliki game atau DLC.")
            return

        temp = self.head
        if temp.id_game == id_game_sebelum:
            print("ID game sebelumnya tidak valid untuk menghapus di antara node.")
            return

        while temp.next:
            if temp.next.id_game == id_game_sebelum:
                temp.next = temp.next.next
                print("Game atau DLC berhasil dihapus dari Steam.")
                return
            temp = temp.next

        print(f"Game dengan ID {id_game_sebelum} tidak ditemukan.")

def main():
    game_steam = GameSteam()

    while True:
        print("\nPilihan Menu:")
        print("1. Tambah Game/DLC di awal")
        print("2. Tambah Game/DLC di akhir")
        print("3. Tambah Game/DLC di antara")
        print("4. Tampilkan Game/DLC")
        print("5. Perbarui Game/DLC")
        print("6. Hapus Game/DLC di awal")
        print("7. Hapus Game/DLC di akhir")
        print("8. Hapus Game/DLC di antara")
        print("9. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            id_game = input("Masukkan ID game: ")
            judul = input("Masukkan judul game: ")
            genre = input("Masukkan genre game: ")
            harga = float(input("Masukkan harga game: "))
            tipe = input("Masukkan tipe (Games/DLC): ")
            game_steam.tambah_game_awal(id_game, judul, genre, harga, tipe)
        elif pilihan == '2':
            id_game = input("Masukkan ID game: ")
            judul = input("Masukkan judul game: ")
            genre = input("Masukkan genre game: ")
            harga = float(input("Masukkan harga game: "))
            tipe = input("Masukkan tipe (Games/DLC): ")
            game_steam.tambah_game_akhir(id_game, judul, genre, harga, tipe)
        elif pilihan == '3':
            id_game_sebelum = input("Masukkan ID game sebelumnya: ")
            id_game_baru = input("Masukkan ID game baru: ")
            judul = input("Masukkan judul game: ")
            genre = input("Masukkan genre game: ")
            harga = float(input("Masukkan harga game: "))
            tipe = input("Masukkan tipe (Games/DLC): ")
            game_steam.tambah_game_di_antara(id_game_sebelum, id_game_baru, judul, genre, harga, tipe)
        elif pilihan == '4':
            game_steam.tampilkan_game()
        elif pilihan == '5':
            id_game = input("Masukkan ID game yang akan diperbarui: ")
            judul = input("Masukkan judul baru (biarkan kosong jika tidak ingin mengubah): ")
            genre = input("Masukkan genre baru (biarkan kosong jika tidak ingin mengubah): ")
            harga = input("Masukkan harga baru (biarkan kosong jika tidak ingin mengubah): ")
            tipe = input("Masukkan tipe baru (biarkan kosong jika tidak ingin mengubah): ")
            if judul or genre or harga or tipe:
                game_steam.perbarui_game(id_game, judul, genre, harga, tipe)
            else:
                print("Tidak ada perubahan yang dilakukan.")
        elif pilihan == '6':
            game_steam.hapus_game_awal()
        elif pilihan == '7':
            game_steam.hapus_game_akhir()
        elif pilihan == '8':
            id_game_sebelum = input("Masukkan ID game sebelumnya: ")
            game_steam.hapus_game_di_antara(id_game_sebelum)
        elif pilihan == '9':
            print("Terima kasih telah memperbaiki data ku (｡˃ ᵕ < ) -Steam ")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()
