from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_summary(self):
        return "Hunian Apartemen." + "\n" + "Jumlah Kamar: " + str(self.jml_kamar) +".\n" +"Jumlah Penghuni: " + str(self.jml_penghuni) + ".\n" + "Dokumen: " + str(self.get_dokumen())
    
    #def get_detail(self):
        #return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\n"
    
    def get_preview(self):
        return "https://awsimages.detik.net.id/community/media/visual/2017/09/08/5c72c356-2fbf-4005-bd91-982c12337319.jpg?w=700&q=90"