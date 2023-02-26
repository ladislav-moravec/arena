from arena import Kostka
from arena import Bojovnik

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
bojovnik = Bojovnik("Zalgoren", 100, 20, 10, kostka)
print("Bojovník: {0}".format(bojovnik)) # test __str__()
print("Naživu: {0}".format(bojovnik.nazivu)) # test  nazivu()
print("Život: {0}".format(bojovnik.graficky_zivot())) # test graficky zivot()
