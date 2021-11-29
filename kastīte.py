class Rekins:

  def __init__(self,klients,veltijums,izmeri,materials):
    self.klients = klients
    self.veltijums = veltijums
    self.izmeri = izmeri
    self.materials = materials

    self.teksta_gar = len(self.veltijums)
    self.izmeri_sar = self.izmeri.split(",")

    self.garums = self.izmeri_sar[0]
    self.platums = self.izmeri_sar[1]
    self.augstums = self.izmeri_sar[2]

  def izdrukat(self):
    pass

  def aprekins(self):
    darba_samaksa = 15 
    PVN = 21 
    produkta_cena = (self.teksta_gar) * 1.2 + (self.platums/100 * self.garums/100 * self.augstums/100)/ 3 * self.materials 
    PVN_summa = (produkta_cena + darba_samaksa)*PVN/100     
    rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa

    return rekina_summa
    
klients = input("Uzraksti savu vārdu un uzvārdu: ")
veltijums = input("Uzraksti veltījumu: ")
izmeri = input("Ievadi lādītes izmērus\n Garums,platums,augstums (raksti veselus skaitļus, atdalot tos ar komatiem\n")
materials = input("Materiāla cena EUR/m2: ")

rekins = Rekins(klients,veltijums,izmeri,materials)
print(rekins.klients)
print(rekins.veltijums)
print(rekins.izmeri)
print(rekins.izmeri_sar)

print(rekins.aprekins())

# print(izmeri)
# print(type(izmeri))
# print(izmeri.split(","))
# sadal = izmeri.split(",")
# print(sadal[0])
# print(sadal[1])
# print(sadal[2])





 