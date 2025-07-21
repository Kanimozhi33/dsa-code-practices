def bin_to_hex (binary):
    # """
    # Convert a binary number to its hexadecimal representation.
    
    # :param binary: A string representing a binary number (e.g., '1101').
    # :return: A string representing the hexadecimal equivalent of the binary number.
    # """
    # try:
    #     # Convert binary to decimal, then to hexadecimal
    #     decimal_num = int(binary, 2)
    #     hex_num = hex(decimal_num)[2:].upper()  # Remove the '0x' prefix and convert to uppercase
    #     return hex_num
    # except ValueError:
    #     return "Invalid binary number"
    binary_dict = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }
    hex = ''
    for i in range (0, len(binary),4):
        group = binary[i:i+4]
        hex += binary_dict[group]
    return hex
