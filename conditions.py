vek = int(input("Zadaj svoj vek: "))

if vek < 18:
    print("Si mladistvý.")
elif vek == 18:
    print("Práve si dosiahol plnoletosť.")
else:
    print("Si dospelý.")
