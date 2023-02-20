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
