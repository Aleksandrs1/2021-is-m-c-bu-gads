#OOP-22.11.

#Te jābūt programmas aprakstam

klients = input("Ievadi savu vārdu un uzvārdu: ")
veltijums = input("Raksti savu veltījumu: ")
izmers = input("Lādītes izmēri:\n platums, garums, augstums\n Raksti veselus skatiļus un atdali tos ar komatiem:\n")
materials = input("Ievadi materiāla cenu EUR/m2: ")

class Rekins:

    def __init__(self,klients,veltijums,izmers,materials):

        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials

        self.veltijuma_gar = len(self.veltijums)
        self.izmeru_sar = self.izmers.split(",")
        self.platums = self.izmeru_sar[0]
        self.garums = self.izmeru_sar[1]
        self.augstums = self.izmeru_sar[2]


    def izdrukat(self):
        pass

    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        produkta_cena = (self.veltijuma_gar) * 1.2 + (self.platums/100 * self.garums/100 * self.augstums/100)/ 3 * self.materials 
        PVN_summa = (produkta_cena + darba_samaksa)*PVN/100 
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa

print(izmers)

print(type(izmers))
print(izmers.split(","))
sad = izmers.split(",")
print(sad[0])


# a = Rekins(klients, veltijums,izmers,materials)

# print(a.veltijuma_gar)