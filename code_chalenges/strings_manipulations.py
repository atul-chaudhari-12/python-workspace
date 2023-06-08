"""
String Manipulations
"""
import re

class StringManipulationClass():

    def checkIfPalindromeUsingExtendedSlicing(self, input_string):     
        input_string = input_string.replace(" ", "").lower()   
        return input_string == input_string[::-1]
    
    def checkPalindrome(self, input_string):
        input_string = input_string.replace(" ", "").lower()   
        length_of_string = len(input_string)
        for i in range(length_of_string//2):
            if input_string[i] != input_string[length_of_string - i - 1]:
                return False
        return True
    
    def removeSpecialCharactersFromString(self, input_string):
        output_string = ""
        for letter in input_string.lower():
            if (ascii(letter) >= ascii("a") and ascii(letter) <= ascii("z")) or ascii(letter)==ascii(" "):
                output_string = output_string + letter
        return output_string
    
    def removeSpecialCharactersFromStringUsingRegularExpression(self, input_string):
        string_pattern = r"[^a-zA-Z0-9\s]"
        processed_string = re.sub(string_pattern, '', input_string)
        return processed_string
    
    def rearrangeSentenceInReverceOrderOfWords(self, input_string):
        return " ".join(input_string.split()[::-1])

if __name__=="__main__":
    obj = StringManipulationClass()
    print("========== Pandrome Check ===========")    
    print (obj.checkIfPalindromeUsingExtendedSlicing("racecar"))
    print (obj.checkIfPalindromeUsingExtendedSlicing("Able was I saw Elba"))
    print (obj.checkIfPalindromeUsingExtendedSlicing("heathly"))
    print (obj.checkIfPalindromeUsingExtendedSlicing("Atul chaudhari"))
    print("=======================================")
    print (obj.checkPalindrome("racecar"))
    print (obj.checkPalindrome("Able was I saw Elba"))
    print (obj.checkPalindrome("heathly"))
    print (obj.checkPalindrome("Atul chaudhari"))
    print("=================remove special characters==========")
    print(obj.removeSpecialCharactersFromString("apples are & found% ony @red & green"))
    print(obj.removeSpecialCharactersFromStringUsingRegularExpression("apples are & found% ony @red & green"))
    print("==========Reverse the Sentence============")
    print(obj.rearrangeSentenceInReverceOrderOfWords("Sky Is Blue"))

