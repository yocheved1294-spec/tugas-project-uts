class Lagu:
    def __init__(self, judul, penyanyi):
        self.judul = judul
        self.penyanyi = penyanyi

    def info_lagu(self):
        return f"Lagu berjudul {self.judul} dinyanyikan oleh {self.penyanyi}"


class Playlist:
    def __init__(self, nama_playlist):
        self.nama_playlist = nama_playlist
        self.daftar_lagu = []

    def tambah_lagu(self, lagu_baru):
        self.daftar_lagu.append(lagu_baru)
        print(f"Lagu berhasil ditambahkan ke {self.nama_playlist} : {lagu_baru.info_lagu()}")

    def tampilkan_semua(self):
        print(f"\n--- Daftar lagu di Playlist: {self.nama_playlist} ---")
        if not self.daftar_lagu:
            print("Playlist kosong.")
        for i, lagu in enumerate(self.daftar_lagu, 1):
            print(f"{i}. {lagu.info_lagu()}")


if __name__ == "__main__":
    my_playlist = Playlist("Lagu Favorit")
    lagu1 = Lagu("The Cure", "OLIVIA RODRIGO")
    lagu2 = Lagu("LANY", "XXL")
    lagu3 = Lagu("Photograph", "Ed Sheeran")

    my_playlist.tambah_lagu(lagu1)
    my_playlist.tambah_lagu(lagu2)
    my_playlist.tambah_lagu(lagu3)

    my_playlist.tampilkan_semua()