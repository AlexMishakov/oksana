print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # (x ≡ ( w ∨ y)) ∨ ((w → z ) ∧ (y → w))
                # ∨ - or
                # ∧ - and
                # ≡ - ==
                # → - <=
                # (not())
                f = (x == (w or y)) or ((w <= z) and (y <= w))
                if f == 0:
                    print(x, y, z, w)

"""
x y z w
0 0 0 1
0 1 0 0
0 1 0 1
0 1 1 0
"""