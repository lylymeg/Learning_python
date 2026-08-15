import random

dice_art = {
    1: (
        "┌───────────────┐",
        "│               │",
        "│               │",
        "│       ●       │",
        "│               │",
        "│               │",
        "└───────────────┘",
    ),
    2: (
        "┌───────────────┐",
        "│  ●            │",
        "│               │",
        "│               │",
        "│               │",
        "│            ●  │",
        "└───────────────┘",
    ),
    3: (
        "┌───────────────┐",
        "│  ●            │",
        "│               │",
        "│       ●       │",
        "│               │",
        "│            ●  │",
        "└───────────────┘",
    ),
    4: (
        "┌───────────────┐",
        "│  ●         ●  │",
        "│               │",
        "│               │",
        "│               │",
        "│  ●         ●  │",
        "└───────────────┘",
    ),
    5: (
        "┌───────────────┐",
        "│  ●         ●  │",
        "│               │",
        "│       ●       │",
        "│               │",
        "│  ●         ●  │",
        "└───────────────┘",
    ),
    6: (
        "┌───────────────┐",
        "│  ●         ●  │",
        "│               │",
        "│  ●         ●  │",
        "│               │",
        "│  ●         ●  │",
        "└───────────────┘",
    ),
}

dice = []
num_of_d = int(input("How many dice?: "))
mode = input("Display mode - (H)orizontal or (V)ertical?: ").strip().upper()

# Lancer les dés
for _ in range(num_of_d):
    dice.append(random.randint(1, 6))

print()

if mode == "V":
    # --- AFFICHAGE VERTICAL ---
    for die in dice:
        for line in dice_art[die]:
            print(line)
        print()  # Ligne vide entre chaque dé
else:
    # --- AFFICHAGE HORIZONTAL ---
    for line in range(7):
        for die in dice:
            print(dice_art[die][line], end="  ")
        print()

print(f"\nTotal: {sum(dice)}")