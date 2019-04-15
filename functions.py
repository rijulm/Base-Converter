import copy

global symbols
symbols = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def base_to_dec(string,base):
    try:
        value = 0
        for place in range(len(string)):
            if symbols.index(string[place]) > base-1:
                return ("INVALID INPUT")
            value += symbols.index(string[place].upper())* (base**((len(string)-1)-place))
        return value
    except:
        return ("INVALID INPUT")

def dec_to_base(string,base):
    try:
        string=int(string)

        value = 0
        count = 0
        placelimit = 0

        output = []

        while value < int(string):
            value = (base ** (placelimit))-1
            placelimit += 1

        placelimit -= 1
        print("placelimit",placelimit)


        for i in range(placelimit):
            output.append("0")

        for place in range (placelimit):
            for placevalue in range(base):
                copyout = copy.copy(output)
                copyout[place] = symbols[placevalue]
                if base_to_dec("".join(copyout),base) > int(string):
                    break
                else:
                    output = copyout
        return ("".join(output))
    except:
        return ("INVALID INPUT")


