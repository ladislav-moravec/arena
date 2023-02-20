from arena import Kostka

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
