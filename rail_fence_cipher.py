def three_rail_encode(string):
    string_list = []
    
    top_rail = []
    mid_rail = []
    bot_rail = []

    for letter in string:
        string_list.append(letter)

    length = len(string_list)

    for i in range(0,length):
        if (i % 2) == 1:
            mid_rail.append(string_list[i])

        ## if odd index / 2 
        elif ((i/2) % 2) == 1:
            bot_rail.append(string_list[i])
        
        else:
            top_rail.append(string_list[i])

    # for letter in string_list:
    #     index = string_list.index(letter)

    #     ## if odd index
    #     if (index % 2) == 1:
    #         mid_rail.append(letter)

    #     ## if odd index / 2 
    #     elif (index/2 % 2) == 1:
    #         bot_rail.append(letter)
        
    #     else:
    #         top_rail.append(letter)

    top_code = ''.join(top_rail)
    mid_code = ''.join(mid_rail)
    bot_code = ''.join(bot_rail)

    encoded = top_code + mid_code + bot_code

    return encoded


coded = three_rail_encode('WEAREDISCOVEREDFLEEATONCE')

print(coded)

if coded == 'WECRLTEERDSOEEFEAOCAIVDEN':
    print('it worked!')

"""
0 = top
1 = mid
2 = bot
3 = mid
4 = top
5 = mid
6 = bot
7 = mid
8 = top

top = 0,4,8,12 (mult of 4?)
mid = odd
bot = 2,6,10,

if index = odd -> mid
if index/2 = even -> top
else = bot
"""