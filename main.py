from arena import Kostka
from arena import Bojovnik
from arena import Arena

sestistenna = Kostka()
desetistenna = Kostka(10)
# nebo = Kostka(pocet_sten=10)

# Hod sestistennou
print(sestistenna)
for _ in range(6):
    print(sestistenna.hod(), end=" ")
# Hod desetistennou
print("\n", desetistenna, sep=" ")
for _ in range(10):
    print(desetistenna.hod(), end=" ")

kostka = Kostka(10)

print(" \n\n")
bojovnik = Bojovnik("Zalgoren", 100, 20, 10, kostka)
print("Život: {0}".format(bojovnik.graficky_zivot())) #test graficky_zivot()
#útok na našeho bojovníka
souper = Bojovnik("Shadow", 60, 18, 15, kostka)
souper.utoc(bojovnik)
print(souper.vrat_posledni_zpravu())
print(bojovnik.vrat_posledni_zpravu())
print("Život: {0}".format(bojovnik.graficky_zivot()))

kostka = Kostka(10)
zalgoren = Bojovnik("Zalgoren", 100, 20, 10, kostka)
shadow = Bojovnik("Shadow", 60, 18, 15, kostka)
arena = Arena(zalgoren, shadow, kostka)
# zápas
arena.zapas()
