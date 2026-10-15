bit_string = input()

while bit_string != "":
    if len(bit_string) != 8:
        print("Error: Input must be exactly 8 bits")
    else:
        ones_count = bit_string.count("1")

        # Even parity: the parity bit must make the total number of 1s even
        if ones_count % 2 == 0:
            parity_bit = 0
        else:
            parity_bit = 1

        print(f"Parity bit: {parity_bit}")

    bit_string = input()
