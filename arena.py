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

        def __str__(self):
            return str(self.__jmeno)
