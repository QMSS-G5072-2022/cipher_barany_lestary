

def cipher_ljb2185(text, shift, encrypt=True):
    """
    The cipher function converts the supplied text into an encrypted string
    based on the amount of shifts in the alphabet.
    For instance, if the letter is "a" and the shift is 3,
    the function should return "d".
    
    Parameters
    -------
    
    text: the original text or the text the user wants to encrypt (type: string)
    shift: the amount of shifts desired by the user in the alphabet (type: integer)
    encrypt: modifying the text in either the process of encryption or decryption (type: boolean)
    
    Returns
    -------
    The encrypted or decrypted new text

    Examples
    --------
    >>> from cipher_ljb2185 import cipher_ljb2185
    >>> cipher_ljb2185.cipher("example", 1, encrypt = True)
        "fybnqmf"
    >>> cipher_ljb2185.cipher("fybnqmf", 1, encrypt = False)
        "example"
    """
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text