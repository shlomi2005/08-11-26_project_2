import random


def play_round(name, rounds):
    start = rounds
    resolt = []

    for i in range(int(start)):
        play_s = roll_dice()
        play_c = roll_dice()
        if play_s > play_c:
            winer = name
        elif play_c > play_s:
            winer = "Computer"
        else:
            winer = "draw"
        resolt.append({
            "round": i+1,
            "player_dice": play_s,
            "computer_dice": play_c,
            "winner": winer
        })

    return resolt


def calculate_winner_user(name, result):
    caunt_w_user = 0
    for dict in result:
        if dict["winner"] == name:
            caunt_w_user += 1
    return caunt_w_user


def calculate_winner_compyutr(result):
    caunt_w_compyutr = 0
    for dict in result:
        if dict["winner"] == "Computer":
            caunt_w_compyutr += 1
    return caunt_w_compyutr


def ween_all(name, win_user, win_com):
    wean_all1 = ""
    if win_user > win_com:
        wean_all1 = name
    elif win_com > win_user:
        wean_all1 = "Computer"
    else:
        wean_all1 = "Draw"
    return wean_all1


def crieit_dict(name, rounds, caunt_w_user, caunt_w_compyutr, wean_all, result):
    all = []
    all.append({"player_name": name, "rounds": rounds, "player_score": caunt_w_user,
               "computer_score": caunt_w_compyutr, "winner": wean_all, "result": result})
    return all


def roll_dice():
    num = random.randint(1, 6)
    return num


def input_name():
    name = input("enter a name ")
    return name


def input_round():
    round = input("enter a number rounds: ")
    return round
