##########################################################################
# 
# Ziv Lempel
# Calvin Grant
# 12/9/22
# 
##########################################################################
# Ziv lempel class
class ZivLempel:
    # initializing the ziv lempel encoded message (as a list)
    # substring (in binary)
    # the final character
    # the output 
    def __init__(self):
        self.ziv = []
        self.substring = ""
        self.compressed = ""
        self.character = ""
    
    # allowing for the string representation of a object 
    def __str__(self):
        return self.compressed 
    
    # converting decimal to binary 
    def convertToBinary(self, char):
        return bin(char).replace("0b", "")
    
    # convert list of ascii character input, to a binary string
    # Alex gave me the idea for this I was only using one conversion before he gave me assistance
    # was having issues getting a list to a string representation
    def BinaryString(self, string):
        myList = [ord(j) for j in string]
        for j in myList:
            # making sure binary representation
            binNum = bin(j).replace("0b", "")
            # while the length is less than eight add zeros to the front of the value to format for eight bits 
            while len(binNum) < 8:
                binNum = "0"+binNum
            # set this as substring  
            self.substring += binNum    

    # function that converts to encoded string 
    def execute(self, my_str):
        subStrTble = []
        self.BinaryString(my_str)
        j = 1
        
        # while the starting string's lenth in greater than zero
        # take unique slices of the string into substrings and increase the counter making sure each slice is unique
        while (len(self.substring) > 0):
            # making sure of unique slices of the string 
            if (self.substring[0 : j] in subStrTble):
                j += 1
            
            # adding the unique slice to the subStrTable (list) and "resetting" the counter
            if (self.substring[0 : j] not in subStrTble):
                subStrTble.append(self.substring[0 : j])
                self.substring = self.substring[j : ]
                j = 1
            
            # this is just made for the final substring, if it is already in the subStrTble find it in the subStrTble
            # pass this value into a temp varible and place this value at the end of the list
            # Alex also helped me with this I kept getting a problem with my first initial if statement it would just continuously keep running (adding to the counter j) without presenting me without ouput
            # he helped by reworking my if statements; changing them from if and elif statements and adding this final if statement to allow for the final character to be accounted for 
            if (j == len(self.substring) + 1 and self.substring[0 : j] in subStrTble):
                lastBits = subStrTble.index(self.substring[0 : j])
                temp = subStrTble[lastBits]
                subStrTble.append(temp)
                self.substring = self.substring.replace(self.substring[0 : j], "")
         
        # for each value in the subStrTble (list)
        # if the length is greater than one convert this number to binary 
        for j in subStrTble:
            if len(j) > 1:
                numericalRep = subStrTble.index(j[ : -1]) + 1
                numericalStr = self.convertToBinary(numericalRep)
                finalInd = j[-1]
                # and append it at the end of the list 
                self.ziv.append(numericalStr + finalInd)
            else:
                self.ziv.append(j)
                
        # calling the function that show the ziv lempel message 
        self.returncompressed()
    
    # this function formats the ziv lempel message 
    def returncompressed(self):
        # initializing variable
        compressed = ""
        
        # for each value in the list
        for j in self.ziv:
            # see if the length of that value is greater than one, voiding the first two and last value of the list
            if len(j) > 1:
                # making sure the values are now put into eight bit representation
                # by adding a 0 to the front until the length of the value is eight 
                while len(j) < 8:
                    j = "0" + j
                compressed += j + " " 
            else:
                compressed += j + " "
                
        # allowing for restult to be returned 
        self.compressed = compressed
            
########
##MAIN##
########
# opens the file and reads line by line
# program will only run with input file
with open("sampleText.txt" , "r" ) as f:
    lines = f.read().splitlines()
# allowing the lines to be read as input one line at a time
for line in lines:
    line = line.rstrip("\n")
    # calling my ZivLempel class
    zivlempel = ZivLempel()
    # calling the execute function passing in the line of text 
    zivlempel.execute(line)
    
# then print the result 
print(zivlempel)