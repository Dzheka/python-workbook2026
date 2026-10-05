# Read bit strings until blank line
bit_string = input()

while bit_string != "":
    # Check if input is exactly 8 bits
    if len(bit_string) != 8:
        print("Error: Input must be exactly 8 bits")
    else:
        # Count the number of 1s
        ones_count = bit_string.count("1")

        # Determine parity bit for even parity
        if ones_count % 2 == 0:
            parity_bit = 0
        else:
            parity_bit = 1

        print(f"Parity bit: {parity_bit}")

    # Read next bit string
    bit_string = input()
