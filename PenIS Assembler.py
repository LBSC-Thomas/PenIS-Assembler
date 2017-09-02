#This is the PenIS assembler, made by LBSC (Thomas)

import sys

#This part are functions that check somethings.
def is_a_function(symbol):
    if symbol == "NOP" or "ADD" or "SUB" or "NAND" or "JMP" or "LD":
        return True
    else:
        return False

def is_a_destination(symbol):
    if symbol == "R0" or "R1" or "R2" or "R3":
        return True
    else:
        return False

def is_a_source(symbol):
    if symbol == "R0," or "R1," or "R2," or "R3,":
        return True
    else:
        return False

def is_a_target(symbol):
    if symbol == "[0]" or "[1]" or "[2]" or "[3]":
        return True
    else:
        return False

def is_a_value(symbol):
    if symbol == "$0" or "$1" or "$2" or "$3" or "$4" or "$5" or "$6" or "$7" or  "$8" or "$9" or "$10" or "$11" or "$12" or "$13" or "$14" or "$15":
        return True
    else:
        return False

def is_a_condition(symbol):
    if symbol == "EQ" or "NEQ" or "NEG" or "JMP":
        return True
    else:
        return False

def is_a_comment(symbol):
    if "//" in symbol:
        return True
    else:
        return False

#This part keeps track of the lines and index for the instruction list. It also indicates which type of instruction it is*.
programCounter = 0
elementInit = 0
instIndicator = ""

#This is the instruction set layed out and all the possible values, since I'm lazy to make an algorithm that converts
#decimal to binary, I'll just use a classic lookup table.
function = {"NOP":"000", "ADD":"001", "SUB":"010", "NAND":"011", "JMP":"100", "LD":"101"}
registers = {"R0":"00", "R1": "01", "R2": "10", "R3":"11"}
condition = {"EQ":"00", "NEQ":"01", "NEG":"10", "JMP":"11"}
values = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000",
          "9":"1001", "10":"1010", "11":"1011", "12":"1100", "13":"1101", "14":"1110", "15":"1111"}

#This part imports the xxx.pen file.
fileImport = input("Type the directory for the file you want to assemble")
if not(".pen" in fileImport):
    fileOpen = open(fileImport, "r")
    fileRead = fileOpen.read()
    fileLoad = str(fileRead)

    #This part creates the xxx.bin file (the output one)
    fileReassign = fileImport.replace(".pen","")
    outputProgram = open(fileReassign, "w+")

    # This part splits the file by lines and spaces.
    for lines in fileLoad.split("\n"):
        instruction = lines.split(" ")

    # This part does the translation (Symbolic Code -> Binary Code)
    # FOR GOD SAKE THOMAS IF THEY FAIL, SET THEM TO ZEROOOOO! Psst: Indicator.
    for sym in instruction:
        if is_a_function(instruction[elementInit]) == True:
            functionSector = function[instruction[elementInit]]
            # instIndicator = 0
            # elementInit +=1
            if instruction[elementInit] == "NOP":
                instIndicator = -1
            elif instruction[elementInit] == "ADD":
                instIndicator = -2
            elif instruction[elementInit] == "SUB":
                instInidcator = -3
            elif instruction[elementInit] == "NAND":
                instIndicator = -4
            elif instruction[elementInit] == "JMP":
                instIndicator = -5
            elif instruction[elementInit] == "LD":
                instIndicator = -6

        elif is_a_source(instruction[elementInit]) == True:
            functionSector = "000"
            sourceSector = registers[instruction[elementInit]]
            instIndicator = 1
            elementInit += 1

        elif is_a_destination(instruction[elementInit]) == True:
            sourceSector = "00"
            destinationSector = registers[instruction[elementInit]]
            instIndicator = 2
            elementInit += 1

        elif is_a_condition(instruction[elementInit]) == True:
            destinationSector = "00"
            conditionSector = condition[instruction[elementInit]]
            instIndicator = 3
            elementInit += 1

        elif is_a_target(instruction[elementInit]) == True:
            conditionSector = "00"
            targetSector = values[instruction[elementInit]]
            instIndicator = 4
            elementInit += 1

        elif is_a_value(instruction[elementInit]) == True:
            targetSector = "00"
            valueSector = values[instruction[elementInit]]
            instIndicator = 5
            elementInit += 1

        elif is_a_comment(instruction[elementInit]) == True:
            valueSector = "0000"
            del instruction[elementInit]
            instIndicator = 6
            elementInit += 1

        else:
            if instIndicator == -1:  # NoOP
                outputString = "0000000"
                outputProgram.write(outputString + "\n")
            elif instIndicator == -2:  # Add
                outputString = functionSector + sourceSector + destinationSector
                outputProgram.write(outputString + "\n")
            elif instIndicator == -3:  # Sub
                outputString = functionSector + sourceSector + destinationSector
                outputProgram.write(outputString + "\n")
            elif instIndicator == -4:  # Nand
                outputString = functionSector + sourceSector + destinationSector
                outputProgram.write(outputString + "\n")
            elif instIndicator == -5:
                outputString = functionSector + targetSector + conditionSector
                outputProgram.write(outputString + "\n")
            elif instIndicator == -6:
                outputString = functionSector + valueSector
                outputProgram.write(outputString + "\n")

else:
    print("Error: this file couldn't be parsed. Please import a file with the .pen extension")