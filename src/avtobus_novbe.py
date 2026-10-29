yaslilar = []
normallar = []

def sernisin_elave_et(ad, yas):
    if yas > 65:
        yaslilar.append((ad, yas))
    else:
        normallar.append((ad, yas))

def avtobusa_mindir():
    if yaslilar:
        return yaslilar.pop(0)
    if normallar:
        return normallar.pop(0)
    return None

def siyahini_goster():
    print("Yaşlılar:", yaslilar)
    print("Normallar:", normallar)

# Test
sernisin_elave_et("Kamran", 65)  # 65 yaş -> Normal növbə
sernisin_elave_et("Qulu", 72)     # 72 yaş -> Prioritet növbə
sernisin_elave_et("Aysel", 22)    # 22 yaş -> Normal növbə
siyahini_goster()

print("Mindi:", avtobusa_mindir())  # Qulu (72)
print("Mindi:", avtobusa_mindir())  # Kamran (65)
siyahini_goster()
