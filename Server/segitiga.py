def segitiga(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Tidak ada segitiga yang dapat dibangun"
    if a >= b + c or b >= a + c or c >= a + b:
        return "Tidak ada segitiga yang dapat dibangun"
    if a == b and b == c:
        return "Segitiga sama sisi"
    if a == b or b == c or a == c:
        return "Segitiga sama kaki"
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Segitiga siku-siku"
    return "Segitiga bebas"
