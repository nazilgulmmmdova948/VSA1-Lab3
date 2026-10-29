novbe = []

def musteri_elave_et(ad, derman):
    novbe.append((ad, derman))

def musteri_cixar():
    if novbe:
        return novbe.pop(0)
    return None

def novbeni_goster():
    for ad, derman in novbe:
        print(ad, "-", derman)

# Test
musteri_elave_et("Murad", "Aspirin")
musteri_elave_et("Nərgiz", "Parasetamol")
novbeni_goster()
print("Xidmət aldı:", musteri_cixar())
novbeni_goster()
