def R(n):
    bn = bin(n)[2:]
    bn = bn + str(bn.count("1") % 2)
    bn = bn + str(bn.count("1") % 2)
    return int(bn, 2)


for n in range(100):
    r = R(n)
    if r > 43:
        print(n, r)
        break
