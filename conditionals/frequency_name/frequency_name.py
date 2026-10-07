"""Write a program that classifies electromagnetic radiation based on its frequency.

Electromagnetic Radiation Classifications
Name	Frequency Range (Hz)
Radio Waves	Less than 3 × 10⁹
Microwaves	3 × 10⁹ to less than 3 × 10¹²
Infrared Light	3 × 10¹² to less than 4.3 × 10¹⁴
Visible Light	4.3 × 10¹⁴ to less than 7.5 × 10¹⁴
Ultraviolet Light	7.5 × 10¹⁴ to less than 3 × 10¹⁷
X-Rays	3 × 10¹⁷ to less than 3 × 10¹⁹
Gamma Rays	3 × 10¹⁹ or more"""

freq = float(input("Enter frequency in Hz: "))

if freq < 3e9:
    print("Radio Waves")
elif freq < 3e12:
    print("Microwaves")
elif freq < 4.3e14:
    print("Infrared Light")
elif freq < 7.5e14:
    print("Visible Light")
elif freq < 3e17:
    print("Ultraviolet Light")
elif freq < 3e19:
    print("X-Rays")
else:
    print("Gamma Rays")