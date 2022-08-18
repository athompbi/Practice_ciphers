import math

def top_rail(string, rails):
    string_list = list(string)

    length = len(string_list)

    top_rail = []

    interval = (rails - 1) * 2

    upper_range = math.ceil(length/interval)

    for i in range(0,upper_range):
        top_rail.append(string_list[interval * i])

    return top_rail


# def mid_rails(string, rails, rail_num):
#     string_list = list(string)

#     length = len(string_list)

#     mid_rail = []

#     interval = (rails - 1) * 2

#     lower_range = rail_num

#     upper_range = math.ceil(length/interval) * 2

#     for i in range(lower_range, upper_range):


#     return mid_rails

def bot_rail(string, rails):
    string_list = list(string)

    length = len(string_list)

    bot_rail = []

    interval = (rails - 1) * 2

    upper_range = math.floor(length/interval)

    for i in range(0,upper_range):
        bot_rail.append(string_list[(rails - 1) + interval * i])

    return bot_rail


def main():

    string = 'abcdefghijklmnopqrstuvwxyz'
    rails = 3
    top = top_rail(string,rails)

    # mid_rail_count = rails - 2

    # for i in range(1,mid_rail_count):
    #     mid_rail = mid_rails(string,rails,i)


    bot = bot_rail(string,rails)

    print(top)
    print(bot)

main() 
