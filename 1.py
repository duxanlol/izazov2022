cvet = input().split()[-1]
voda = int(input().split()[-1])
djubrivo = int(input().split()[-1])
temperatura = int(input().split()[-1])
stabljika = '-'

temperaturaAdekvatna = temperatura >= 20 and temperatura <= 30
segment = voda * stabljika
if temperaturaAdekvatna:
    segment += djubrivo * cvet
rezultat = segment * voda
if not temperaturaAdekvatna:
    rezultat += cvet
print("Rezultat: " + rezultat)
