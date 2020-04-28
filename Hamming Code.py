# Before running code, please install colorama -- pip install colorama

from colorama import Fore, Back, Style

# Function that checks if number is power of two
def isPowerOfTwo(n):
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0

# Function that gets the positions of check bits
def getPositions(bit):
    bits = list(bit)
    positions = []
    i = 1

    while len(bits) >= 1:
        if isPowerOfTwo(i):
            positions.append(i-1)
            i += 1
        else:
            bits.pop(0)
            i += 1

    return positions

# Function that adds bits to the position of number of power of two
def addBits(bit):
    bits = list(bit)
    return_bits = []
    i = 1

    while len(bits) >= 1:
        if isPowerOfTwo(i):
            return_bits.append(0)
            i += 1
        else:
            return_bits.append(bits.pop(0))
            i += 1

    return return_bits

# Function that checks the check bits
def countSum(bit, skip):
    start_position = bit[skip-1:]
    counter = 0
    amount = 0

    while len(start_position):
        try:
            for i in range(skip):
                amount += start_position[0]
                start_position.pop(0)
            start_position = start_position[skip:]
        except:
            break

    return amount % 2 == 0

# Function that replaces the value of check bit
def replaceValue(bit, power):
    if countSum(bit, power):
        return 0
    else:
        return 1

# Iterate
def iterate(positions, bits):
    for i in range(len(positions)):
        bits[positions[i]] = replaceValue(bits, positions[i]+1)

    return bits


def resetToZero(arr, positions):
    for i in range(len(positions)):
        arr[positions[i]] = 0

    return arr

# find an error
def findError(arr, keep, positions):
    resetToZero(arr, positions)
    iterate(positions, arr)

    sum = 0

    for i in range(len(arr)):
        if arr[i] != keep[i]:
            sum += i+1

    print(arr)
    print(keep)
    if sum != 0:
        return ('Found an error at the position: ' + str(sum))
    else:
        return ('Didnt find an error!')

# Print all stuff
def printAll(data, data_keep):
    arr = []
    keeper = []

    for i in range(len(data)):
        arr.append(int(data[i]))
        keeper.append(int(data_keep[i]))

    white = Fore.WHITE
    red = Fore.RED
    green = Fore.GREEN
    cyan = Fore.CYAN

    print('Initial bits:        ', arr)

    bits = addBits(arr)
    bits_keeper = addBits(keeper)
    keeper_positions = getPositions(keeper)
    positions = getPositions(arr)

    print('Bits with check bits: [', end="")

    for i in range(len(bits)):
        if i in positions:
            print(red, str(bits[i]), end=" ")
        else:
            print(green + str(bits[i]), end=" ")

    print(white, ']')

    iterate(positions, bits)
    iterate(keeper_positions, bits_keeper)

    print('Bits after replacing: [', end="")

    for i in range(len(bits)):
        if i in positions:
            print(red, str(bits[i]), end=" ")
        else:
            print(green + str(bits[i]), end=" ")

    print(white, ']')

    print(findError(bits, bits_keeper, positions))


# Main function for initialize
def main():
    printAll('000010001010', '000010001010')

 # Call main function
if __name__ == "__main__":
    print(main())
