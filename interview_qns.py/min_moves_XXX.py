# min moves to make '000'
def min_moves(arr):
    i = 0
    moves = 0
    while i<len(arr):
        if arr[i] == 'X':
            i+=3
            moves +=1
        else:
            i+=1
    return moves