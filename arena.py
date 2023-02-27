class Kostka:
    """
    Třída reprezentuje hrací kostku.
    """

    # Konstruktor
    def __init__(self, pocet_sten=6):
        # __ dělá z atributu neveřejný,
        # za = je parametr(argument))
        # klicovy argument pocet_sten=6
        self.__pocet_sten = pocet_sten

    def vrat_pocet_sten(self):
        """
        Vrátí počet štěn kostky.
        """
        return self.__pocet_sten

    def hod(self):
        """
        Vykoná hod kostkou a vrátí náhodnou hodnotu od 1 do počtu stěn.
        """
        import random as _random
        return _random.randint(1, self.__pocet_sten)

    def __str__(self):
        """
        Vrací textovou reprezentaci konstky.
        V základu je definován, ale nyní nevrátí cestu ale to, co definujeme.
        """
        return str("Kostka s {0} stěnami".format(self.__pocet_sten))


class Bojovnik:
    """
    Třída reprezentuje bojovníka do arény.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        """
        :param jmeno: jméno bojovnéka
        :param zivot: maximální život bojovníka
        :param utok: útok bojovníka
        :param obrana: obrana bojovníka
        :param kostka: instance kostky
        """
        self.__jmeno = jmeno
        self.__zivot = zivot
        self.__max_zivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kostka = kostka
        self.__zprava = ""

    def __str__(self):
        """
        :return: Jméno bojovníka
        """
        return str(self.__jmeno)

    def __repr__(self):
        """
        :return: V řetězci kód konstruktoru pro funkci eval().
        """
        return str("Bojovnik{0}, {1}, {2}, {3}, {4}".format(self.__jmeno,
                                                            self.__max_zivot,
                                                            self.__utok,
                                                            self.__obrana,
                                                            self.__kostka))

    @property
    def nazivu(self):
        """
        :return: Vrátí True, pokud je bojovník naživu.
        Jinak vrátí False.
        """
        return self.__zivot > 0

    def graficky_zivot(self):
        celkem = 20
        pocet = int(self.__zivot / self.__max_zivot * celkem)
        if pocet == 0 and self.nazivu:
            pocet = 1
        return "[{0}{1}]".format("#" * pocet, " " * (celkem - pocet))

    def bran_se(self, uder):
        zraneni = uder - (self.__obrana + self.__kostka.hod())
        if zraneni > 0:
            zprava = "{0} utrpěl poškození {1} hp.".format(self.__jmeno, zraneni)
            self.__zivot = self.__zivot - zraneni
            if self.__zivot < 0:
                self.__zivot = 0
                zprava = zprava[:-1] + " a zemřel."
            else:
                zprava = "{0} odrazil útok. ".format(self.__jmeno)
            self.__nastav_zpravu(zprava)

    def utoc(self, souper):
        uder = self.__utok + self.__kostka.hod()
        zprava = "{0} útočí s úderem za {1} hp.".format(self.__jmeno, uder)
        self.__nastav_zpravu(zprava)
        souper.bran_se(uder)

    def __nastav_zpravu(self, zprava):
        self.__zprava = zprava

    def vrat_posledni_zpravu(self):
        return self.__zprava
