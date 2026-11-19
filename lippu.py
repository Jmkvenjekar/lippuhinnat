"""Lippuhinnan laskenta – testausharjoituksen testattava koodi.

Vaatimukset:
  - alle 7-vuotiaat matkustavat ilmaiseksi (0 €)
  - 7–17-vuotiaat: lapsilippu 8 €
  - 18–64-vuotiaat: aikuisten lippu 15 €
  - 65-vuotiaat ja vanhemmat: eläkeläislippu 10 €
  - ikä on väliltä 0–120, muuten ValueError
  - ryhmälle (vähintään 10 lippua) myönnetään 10 % alennus kokonaishinnasta
"""

LAPSI_HINTA = 8.0
AIKUINEN_HINTA = 15.0
ELAKELAINEN_HINTA = 10.0
RYHMAN_KOKO = 10
RYHMA_ALENNUS = 0.10
OPISKELIJA_HINTA = 10.0


def lippuhinta(ika, opiskeljia=False):
    """Palauttaa yhden lipun hinnan euroina iän perusteella."""
    if ika < 0 or ika > 120:
        raise ValueError("Ikä on virheellinen")
    if ika < 7:
        return 0.0
    if opiskeljia:
        return OPISKELIJA_HINTA
    if ika <= 17:
        return LAPSI_HINTA
    if ika < 65:
        return AIKUINEN_HINTA
    return ELAKELAINEN_HINTA


def kokonaishinta(iat, opiskelijat=None):
    """Palauttaa lippujen yhteishinnan euroina, ryhmäalennus huomioituna."""
    if opiskelijat is None:
        opiskelijat = [False] * len(iat)
    summa = sum(lippuhinta(ika, opiskelija) for ika, opiskelija in zip(iat, opiskelijat))
    if len(iat) >= RYHMAN_KOKO:
        summa = summa * (1 - RYHMA_ALENNUS)
    return round(summa, 2)
