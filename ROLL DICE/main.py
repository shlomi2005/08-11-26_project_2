from function.afala import afala_1


def menu():
    shlomi = [1, 2, 3, 4]
    print("""================================
          ROLL DICE
================================""")
    while True:
        pick = input("""

1. Start New Game
2. View Game History
3. View Statistics
4. Exit

Choose an option:
""")
        try:
            pick = int(pick)
        except ValueError:
            print("enter a number not a string")
            continue
        if pick not in shlomi:
            print("not a valid number")
            continue
        if pick == 1:
            return (afala_1())
        if pick == 4:
            break


menu()
