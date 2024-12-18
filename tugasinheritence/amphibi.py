# buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu memiliki 2 properti dan method  
#buat 3 objek dari masing masing class child. 

from Animal import Animal

class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal(),
        print("Jenis Air /t/t/t :", self.jenis_air,
              "/Bernapas /t/t/t :", self.bernapas)
        
amphibi = Amphibi("katak","serangga","dua alam", "bertelur", "air tawar", "kulit dan paru paru")
amphibi.info_amphibi()
