# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
# buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu memiliki 2 properti dan method  
#buat 3 objek dari masing masing class child. 

class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

def info_animal(self):
    print(f"Nama Hewan /t/t/t :", self .name)

hewan = Animal("Kucing", "Daging", "10 Tahun", "Mengandung")
hewan.info_animal()