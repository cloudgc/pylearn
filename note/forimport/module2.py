def data(top):
    contain = []
    a, b = 0, 1
    while True:
        if (b >= top):
            return contain
        contain.append(b)
        a, b = b, a + b

