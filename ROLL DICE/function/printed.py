def print_game(name, resolt, ween_all, user, comp):
    for res in resolt:
        print(f"---------- ROUND {res["round"]} ----------")
        print(f"""
{name}:    🎲 {res["player_dice"]}
Computer: 🎲 {res["computer_dice"]}

 {res["winner"]} wins this round!
""")
    print("""================================
          GAME OVER
================================
""")
    print(f"""{name}:    {user} points 
Computer: {comp} points

WINNER: {ween_all}!

Game saved successfully!
""")
