def disemvowel(string_):
    a = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
    x = []
    for i in string_:
        if i in a:
            continue
        else:
            x.append(i)

    return ''.join(x)