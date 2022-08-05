
def caeser_encrypter(string, n):
    """A basic Caeser cipher that takes a string and then moves
    each letter's ascii by n, giving a new character. This cipher
    only affects letters, all other characters are the same as 
    in the original string. 
    
    Return:
        new_string: encrypted string"""

    def get_new_ascii(ascii, n, max):
        """Gets the new ascii for encoding through a cipher. The ascii 
        has n added to it, and if the new ascii is out of range of the max,
        then 26 is subtracted to keep the character a letter.
        
        Return:
            new_ascii: converted ascii"""

        new_ascii = ascii + n
        if new_ascii > max:
            new_ascii -= 26

        return new_ascii

    new_string = ""

    for character in string:

        ascii = ord(character)

        if ascii > 96 and ascii < 123:
            new_string += chr(get_new_ascii(ascii, n, 122))

        elif ascii > 64 and ascii < 91:
            new_string += chr(get_new_ascii(ascii, n, 90))

        else:
            new_string = new_string + character

    return new_string



def caeser_decrypter(string, n):

    def get_new_ascii(ascii, n, max):
        """Gets the new ascii for encoding through a cipher. The ascii 
        has n added to it, and if the new ascii is out of range of the max,
        then 26 is subtracted to keep the character a letter.
        
        Return:
            new_ascii: converted ascii"""

        new_ascii = ascii - n
        if new_ascii > max:
            new_ascii += 26

        return new_ascii

    new_string = ""

    for character in string:

        ascii = ord(character)

        if ascii > 96 and ascii < 123:
            new_string += chr(get_new_ascii(ascii, n, 122))

        elif ascii > 64 and ascii < 91:
            new_string += chr(get_new_ascii(ascii, n, 90))

        else:
            new_string = new_string + character

    return new_string

string = 'Amelia'

### highest encryption factor = 13
### lowest encryption factor = 1

############################################################### why is this breaking after 13?
#### something happening with max in decrypter 


e = 13

encrypted_string = caeser_encrypter(string,e)

print(encrypted_string)

decrypted_string = caeser_decrypter(encrypted_string,e)

print(decrypted_string)
