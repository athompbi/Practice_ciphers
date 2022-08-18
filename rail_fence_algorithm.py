import math

def top_rail(string, rails):
    string_list = list(string)

    length = len(string_list)

    top_rail = []

    interval = (rails - 1) * 2

    ### calculate how many numbers will be in top rail
    ### length / interval then round down?

    upper_range = math.ceil(length/interval)

    for i in range(0,upper_range):
        top_rail.append(string_list[interval * i])

    return top_rail



def mid_rails(string, rails):
    pass

def bot_rail(string, rails):
    pass


print(top_rail('0123456789',5))