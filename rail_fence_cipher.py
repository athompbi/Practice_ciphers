### for decoding
import math


def encode(string):
    """Runs text through the Rail Fence Cipher with 3 rails
    
    Return:
        encoded: encrypted string"""

    ### make string iterable
    string_list =list(string)
    
    ### lists to store rail values
    top_rail = []
    mid_rail = []
    bot_rail = []

    length = len(string_list)

    ### iterate through each letter by index
    for i in range(0,length):

        ### if the index is odd, add to mid rail
        if (i % 2) == 1:
            mid_rail.append(string_list[i])

        ### if the index/2 is odd, add to bottom rail
        elif ((i/2) % 2) == 1:
            bot_rail.append(string_list[i])
        
        ### else, add to the top rail
        else:
            top_rail.append(string_list[i])

    ### put rail lists into strings
    top_code = ''.join(top_rail)
    mid_code = ''.join(mid_rail)
    bot_code = ''.join(bot_rail)

    encoded = top_code + mid_code + bot_code

    return encoded


def decode(string):
    """Runs coded string by Rail Fence cipher with 3 rails
    through a decoder
    
    Return:
        decoded: decrpted string"""

    length = len(string)
    decoded_list = []

    ### determine the length of the rails to find where breaks are
    mid_len = math.floor(length / 2)
    remain_len = length - mid_len
    top_len = math.ceil(remain_len / 2)
    bot_len = remain_len - top_len

    ### first break is just top_len
    sec_break = top_len + mid_len

    ### break string into rails
    top_rail = list(string[0:top_len])
    mid_rail = list(string[top_len:sec_break])
    bot_rail = list(string[sec_break:length])

    ### track how often the mid rail is used
    mid_count = 0

    ### add the indexed character from each rail to decoded_list
    ### only add if the length of the section is greater than the index being called
    for i in range(0,top_len):
        decoded_list.append(top_rail[i])

        if mid_len > mid_count:
            decoded_list.append(mid_rail[mid_count])
            mid_count += 1
        else:
            pass

        if bot_len > i:
            decoded_list.append(bot_rail[i])
        else:
            pass

        if mid_len > mid_count: 
            decoded_list.append(mid_rail[mid_count])
            mid_count += 1
        else:
            pass
        
    ### put list back into string
    decoded = ''.join(decoded_list)

    return decoded
