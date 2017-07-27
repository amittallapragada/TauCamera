def swap16(i):
    return bytearray([ ((i >> 8) & 0xFF), i & 0xFF ])