intab=b'am'
outab=b'77'
table=bytes.maketrans(intab,outab)
a='amzz€'
c=b'amzz\xa4'
print(c.translate(table))
print(c)