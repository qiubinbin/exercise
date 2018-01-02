import struct
print(struct.pack('I3sf',7,b'qiu',2.3))
print(struct.pack('>H',0xabcd,))
print(struct.pack('p',b'qiu'))
