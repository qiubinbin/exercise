def pp():
    m = 0

    def count():
        nonlocal m
        m += 1
        return m

    return count


if __name__ == '__main__':
    a = pp()
    print(a(), a())
