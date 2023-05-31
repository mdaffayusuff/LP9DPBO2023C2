from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_summary(self):
        return "Hunian Rumah." + "\n" + "Jumlah Kamar: " + str(self.jml_kamar) +".\n" +"Jumlah Penghuni: " + str(self.jml_penghuni) + ".\n" + "Dokumen: " + str(self.get_dokumen()) + "."\
    
    def get_preview(self):
        return "https://static-id.lamudi.com/static/media/bm9uZS9ub25l/1000x620/5fdd6bcd379871.jpg"
   