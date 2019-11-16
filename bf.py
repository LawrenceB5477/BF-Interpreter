import sys 

def main(): 
    if len(sys.argv) < 2:
        print("Please specify an input file")
        sys.exit()

    with open(sys.argv[1], "r") as file:
        contents = file.read() 

        ram = [0] 
        index = 0 
        instruction = 0
        inloop = False
        loopstack = [] 
        loopstart = -1 
        loopend = -1 
        
        while instruction < len(contents): 
            char = contents[instruction] 

            if char == ">":
                index += 1 
                if index >= len(ram):
                    ram.append(0)
            elif char == "<":
                index -= 1
                if index < 0:
                    print("Out of bounds!")
                    sys.exit()
            elif char == "+":
                ram[index] += 1
            elif char == "-":
                ram[index] -= 1
            elif char == ".":
                print(chr(ram[index]), end="")
            elif char == ",":
                ram[index] = ord(input()[0])
            elif char == "[":
                if loopstart != instruction:
                    loopstart = instruction
                    
                    #Deals with nested loops
                    startseen = 1 
                    stopseen = 0 
                    
                    while contents[instruction] != "]" or stopseen <= startseen - 1:
                        instruction += 1 
                        if instruction >= len(contents):
                            print("Error, unclosed loop")
                            sys.exit(1)
                        if contents[instruction] == "[":
                            startseen += 1
                        if contents[instruction] == "]":
                            stopseen += 1

                    loopend = instruction
                    instruction = loopstart
                    loopstack.append((loopstart, loopend))
                if instruction == loopstart: 
                    if ram[index] != 0:
                        inloop = True 
                    else:
                        loopstack.pop() 
                        instruction = loopend 
                        if len(loopstack) == 0:
                            inloop = False
                        else:
                            loopstart = loopstack[len(loopstack) - 1][0]
                            loopend = loopstack[len(loopstack) - 1][1]
            elif char == "]": 
                if inloop and instruction == loopend:
                    instruction = loopstart - 1
                else:
                    print("Error! Closing loop with no starting")
                    sys.exit(1) 
            elif char == " ":
                pass
            elif char == "\n":
                pass
            else:
                pass
            instruction += 1

if __name__ == "__main__":
    main() 
