# Mamalia.py

from Animal import Animal

class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_bulu, cara_bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.cara_bernapas = cara_bernapas

    def info_mamalia(self):
        super().info_animal()
        print("Jenis Bulu:", self.jenis_bulu)
        print("Cara Bernapas:", self.cara_bernapas)

# Contoh penggunaan
mamalia = Mamalia("Harimau", "Daging", "Daratan", "Melahirkan", "Bulu Halus", "Paru-paru")
mamalia.info_mamalia()