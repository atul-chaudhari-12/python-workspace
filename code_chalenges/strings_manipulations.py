"""
String Manipulations
1. Check if palindrome
2. Remove special character from string
3. Rearrange sentence is reverce order of words
4. Implement an algorithm to determine if a string has all unique characters.
5. Given two strings, write a method to decide if one is permutation of other
6. Check if given string is palindrome permutation
"""
import re
from collections import Counter

class StringManipulationClass():
    #Solution 1 [a]
    def checkIfPalindromeUsingExtendedSlicing(self, input_string):     
        input_string = input_string.replace(" ", "").lower()   
        return input_string == input_string[::-1]
    
    #Solution 1 [b]
    def checkPalindrome(self, input_string):
        input_string = input_string.replace(" ", "").lower()   
        length_of_string = len(input_string)
        for i in range(length_of_string//2):
            if input_string[i] != input_string[length_of_string - i - 1]:
                return False
        return True
    
    #Solution 2 [a]
    def removeSpecialCharactersFromString(self, input_string):
        output_string = ""
        for letter in input_string.lower():
            if (ascii(letter) >= ascii("a") and ascii(letter) <= ascii("z")) or ascii(letter)==ascii(" "):
                output_string = output_string + letter
        return output_string
    
    #Solution 2 [b]
    def removeSpecialCharactersFromStringUsingRegularExpression(self, input_string):
        string_pattern = r"[^a-zA-Z0-9\s]"
        processed_string = re.sub(string_pattern, '', input_string)
        return processed_string
    
    #Solution 3
    def rearrangeSentenceInReverceOrderOfWords(self, input_string):
        return " ".join(input_string.split()[::-1])

    # Solution 4
    def determineIfStringHasUniqueCharacters(self, input_string):
        """considering ipute string is ascii not unicode"""
        hashMap = {}
        if len(input_string) > 128:
            return "String has duplicate characters"
        for letter in input_string:
            if letter in hashMap.keys():
                return "String has duplicate characters"
            hashMap[letter] = 1
        return "String has Unique characters"

    # Solution 5
    def checkForPermutations(self, input_string1, input_string2):
        """
        Assumptions: 
            1. Case sensitive
        """
        if len(input_string1) != len(input_string2):
            return "Strings are not Permutations of each other"
        stringHashMap = Counter(input_string1)
        for letter in input_string2:
            if letter not in stringHashMap:
                return "Strings are not Permutations of each other"
        return "Its Permutation"    

    # Solution for 6
    def checkIfPalindromePermutation(self, input_string):
        input_string = input_string.replace(" ", "")
        length_of_string = len(input_string)
        stringHashMap = Counter(input_string)
        if length_of_string % 2==0 and set(stringHashMap.values())=={2}:
            return "Yes, Its palindrome Permutation"
        elif length_of_string % 2==1 and Counter(stringHashMap.values())[1]==1 and Counter(stringHashMap.values())[2]==(length_of_string-1)/2:
            return "Yes, Its palindrome Permutation"
        return "No, Its Not palindrome Permutation"


if __name__=="__main__":
    obj = StringManipulationClass()
    # print("========== Pandrome Check ===========")    
    # print (obj.checkIfPalindromeUsingExtendedSlicing("racecar"))
    # print (obj.checkIfPalindromeUsingExtendedSlicing("Able was I saw Elba"))
    # print (obj.checkIfPalindromeUsingExtendedSlicing("heathly"))
    # print (obj.checkIfPalindromeUsingExtendedSlicing("Atul chaudhari"))
    # print("=======================================")
    # print (obj.checkPalindrome("racecar"))
    # print (obj.checkPalindrome("Able was I saw Elba"))
    # print (obj.checkPalindrome("heathly"))
    # print (obj.checkPalindrome("Atul chaudhari"))
    # print("=================remove special characters==========")
    # print(obj.removeSpecialCharactersFromString("apples are & found% ony @red & green"))
    # print(obj.removeSpecialCharactersFromStringUsingRegularExpression("apples are & found% ony @red & green"))
    # print("==========Reverse the Sentence============")
    # print(obj.rearrangeSentenceInReverceOrderOfWords("Sky Is Blue"))

