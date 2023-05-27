import sys
class Searching:
    '''
    Demonstrate Different searcing techniques using python
    '''
    def binary_search(self, sorted_array, num_to_search):  
        """
            1. Expects sorted array as input
            2. Complexity O(log n)
            3. Strings can be compared but make sure all strings are in same case
        """                     
        if len(sorted_array)==0:
            return -1
        start_position = 0
        end_position = (len(sorted_array) - 1)
        mid = 0
        while start_position <=end_position:
            mid = (start_position + end_position)//2
            if sorted_array[mid]==num_to_search:
                return mid
            elif(sorted_array[mid] > num_to_search):
                end_position = mid - 1
            else:
                start_position = mid+1                
            
        return -1
            
            
            
if __name__=='__main__':    
    obj = Searching()
    if(sys.argv[1] == "binary"):
        print (obj.binary_search(sorted(['Atul', 'Kon', 'Ram', 'Shyam', 'Titu']),"Titu"))
        print (obj.binary_search([1,2,3,4,5,6,7,8,9], 3))
        print(obj.binary_search([1,2,3,4,5,6,7,8,9], 1))
        print(obj.binary_search([1,2,3,4,5,6,7,8,9], 8))
        print(obj.binary_search([1,2,3,4,5,6,7,8,9], 9))
        print(obj.binary_search([1,2,3,4,5,6,7,8,9], 90))
            

