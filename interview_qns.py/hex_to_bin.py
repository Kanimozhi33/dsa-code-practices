def hex_to_bin (hex_num):
    """
    Convert a hexadecimal number to its binary representation.
    
    :param hex_num: A string representing a hexadecimal number (e.g., '1A3F').
    :return: A string representing the binary equivalent of the hexadecimal number.
    """
    # try:
    #     # Convert hex to decimal, then to binary
    #     decimal_num = int(hex_num, 16)
    #     binary_num = bin(decimal_num)[2:]  # Remove the '0b' prefix
    #     return binary_num
    # except ValueError:
    #     return "Invalid hexadecimal number"
    hex_dict = {
        "0":"0000", "1": "0001", "2": "0010", "3":"0011","4": "0100", "5": "0101", "6": "0110", "7":"0111",
        "8":"1000", "9": "1001", "A": "1010", "B":"1011","C": "1100", "D": "1101", "E": "1110", "F":"1111"
    }
    hex_num = hex.num.upper()
    bin_num = ''
    for digit in hex_num:
        if digit in hex_dict:
            bin_num += hex_dict[digit]
        else:
            return "Invalid hexadecimal number"
    return bin_num