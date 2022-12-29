def segitiga(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Tidak ada segitiga yang dapat dibangun"
    if a >= b + c or b >= a + c or c >= a + b:
        return "Tidak ada segitiga yang dapat dibangun"
