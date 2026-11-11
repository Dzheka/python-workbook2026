def decimal_to_binary(n):
    bin_n = ""
    while True:
        r = n % 2
        bin_n = str(r) + bin_n
        n = n // 2
        if n == 0:
            return bin_n