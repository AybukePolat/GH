print("""
Toplama islemi icin +,
Cikarma islemi icin -,
Carpma islemi icin *,
Bolme islemi icin /'ye basin.
""")
#eval() ile denenebilir.
veri1 = input("1.sayiyi giriniz")
islem = input("Operator seciniz")
veri2 = input("2.sayiyi giriniz")

if islem == "+":
    sayi1 = int(veri1)
    sayi2 = int(veri2)
    print(sayi1, "+", sayi2, "=", sayi1 + sayi2)

if islem == "-":
     sayi1 = int(veri1)
     sayi2 = int(veri2)
     print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
if islem == "*":
     sayi1 = int(veri1)
     sayi2 = int(veri2)
     print(sayi1, "*", sayi2, "=", sayi1 * sayi2)
if islem == "/":
     sayi1 = int(veri1)
     sayi2 = int(veri2)
     print(sayi1, "/", sayi2, "=", sayi1 / sayi2)