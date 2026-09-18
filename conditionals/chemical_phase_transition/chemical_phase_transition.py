"""Notes
Input should be case-insensitive (handle "SOLID", "Liquid", "GAS", etc.)
Valid phases are: solid, liquid, gas, plasma
If the initial and final phases are the same, display No transition
If the transition is not physically possible (e.g., solid to plasma), display Cannot transition directly
Only the following transitions are possible:
Solid ↔ Liquid (melting/freezing)
Liquid ↔ Gas (vaporization/condensation)
Solid ↔ Gas (sublimation/deposition)
Gas ↔ Plasma (ionization/recombination)"""

state1 = input().lower()
state2 = input().lower()

transitions = {
    ("solid", "liquid"): "melting" ,
    ("liquid", "solid"): "freezing",
    ("solid", "gas" ): "sublimation",
    ("gas", "solid"): "deposition"  ,
    ("liquid", "gas"): "vaporization",
    ("gas", "liquid"): "condensation",
    ("gas", "plasma"): "ionization" ,
    ("plasma", "gas" ): "recombination",
}
valid_phases = ["solid", "liquid", "gas", "plasma"]
if state1 == state2:
    print("No transition")
elif state1 not in valid_phases or state2 not in valid_phases:
    print("Invalid phase entered")
else:
    print(transitions.get((state1, state2), "Cannot transition directly"))