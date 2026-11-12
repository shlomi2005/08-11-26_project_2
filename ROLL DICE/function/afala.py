from function.start_all_game import *
from data.data_function import write_json
from function.printed import print_game


def afala_1():
    input_name1 = input_name()
    num_roun = input_round()
    resoult1 = play_round(input_name1, num_roun)
    nikud_user = calculate_winner_user(input_name1, resoult1)
    nikud_compyuter = calculate_winner_compyutr(resoult1)
    weener_all1 = ween_all(input_name1, nikud_user, nikud_compyuter)
    p = print_game(input_name1, resoult1, weener_all1,
                   nikud_user, nikud_compyuter)

    dict_all = crieit_dict(input_name1, num_roun, nikud_user,
                           nikud_compyuter, weener_all1, resoult1)
    write_json(dict_all)
