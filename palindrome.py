def filter_palindrome(m):
    temp = str(m)
    if temp == temp[::-1]:
        return True
    else:
        return False


a = [121, 123, 14541, 336633, 4561256, 77777, 89598]
print(list(filter(filter_palindrome, a)))
