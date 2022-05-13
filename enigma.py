# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:03:03 2022

@author: Ксения
"""

import string

inputString = open("text.txt", encoding='utf-8').read()
inputString = inputString.upper()
stringByWords = inputString.split()

abc = list(string.ascii_uppercase)

class thirdRotor:
    dictionary = [(1,3),(5,20),(17,2),(2,15),(14,18),(8,1),(12,13)
                ,(18,10),(9,5),(13,24),(3,19),(23,6),(6,17),(16,12),(25,21),
                    (15,26),(4,8),(10,25),(21,9),(26,14),(22,11),(19,16),(11,23),
                           (24,7),(7,4),(20,22)]
    code_position = 0
    decode_position = 0
    
    def code(self, input, direction):       
        self.code_position = self.code_position + 1
        if self.code_position > 26:
            self.code_position = self.code_position - 26
        search = self.cykleSearch((input + self.code_position))
        result = 0
        for i in range(0,26):
            if self.dictionary[i][switchDirection(direction)] == search:
                result = self.dictionary[i][direction]
        return result
    
    def decode(self, input, direction):       
        self.decode_position = self.decode_position + 1
        if self.decode_position > 26:
            self.decode_position = self.decode_position - 26
        real_position = self.decode_position
        if direction == 0:
            real_position = real_position + 1
        else:
            real_position = real_position - 1      
        for i in range(0,26):
            if self.dictionary[i][switchDirection(direction)] == input:
                result = self.dictionary[i][direction] - real_position
                while result <= 0:
                    result = result + 26
        return result
    
    def cykleSearch(self,search):
        while search > 26:
            search = search - 26
        return search

class stator:
    dictionary = [(5,24), (14,19), (9,23), (26,13), (22,7),(20,12),
                           (17,1),(21,25),(16,2),(18,3),(11,8),(10,6),(4,15),(24,5),(19,14),
                           (23,9),(13,26),(7,22),(12,20),(1,17),(25,21),(2,16),(3,18),
                           (8,11),(6,10),(15,4)]
        
    def find(self,input):
        for i in range(0,26):
            if self.dictionary[i][0] == input:
                return self.dictionary[i][1]
                
rotor_3 = thirdRotor()
stator = stator()

def crypt_word(word):
    result = list()
    for letter in word:
        result.append(codeByRotors(letter))
    return result 

def decrypt_word(word):
    result = list()
    for letter in word:
        result.append(decodeByRotors(letter))
    return result 

def codeByRotors(letter):
    number = abc.index(letter) + 1
    thirdRtl = rotor_3.code(number,0)
    statorRtl = stator.find(thirdRtl)
    thirdLtr = rotor_3.code(statorRtl,1)
    
    result = thirdLtr
    return abc[result - 1]

def decodeByRotors(letter):
    number = abc.index(letter) + 1
    thirdRtl = rotor_3.decode(number,0)
    statorRtl = stator.find(thirdRtl)
    thirdLtr = rotor_3.decode(statorRtl,1)
    
    result = thirdLtr
    return abc[result - 1]

def switchDirection(direction):
    return 0 if direction == 1 else 1

result = list()
for word in stringByWords:
    crypted = crypt_word(word)
    result.append(crypted)

crypted_text = str(result)
encode = open("encode.txt",  'w', encoding='utf-8')
encode.write(crypted_text)

result2 = list()
for cryptedWord in result:
    uncr = decrypt_word(cryptedWord)
    #print(uncr)
    result2.append(uncr)
   