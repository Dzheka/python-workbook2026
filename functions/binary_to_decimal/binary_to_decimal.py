def binary_to_decimal(binary):
    binary=binary[::-1]
    des=0
    for i in range(0,len(binary),1):
        des+=int(binary[i])*(2**i)
    return des