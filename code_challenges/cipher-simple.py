def decrypt_string(text, k):
    op_string = ""
    for character in text.lower():
        new_char_ascii = ord(character) - k
        if new_char_ascii < ord("a"):
            new_char_ascii = ord("z") - (ord("a") - new_char_ascii) + 1
        
        
        op_string = op_string + chr(new_char_ascii)
    return op_string