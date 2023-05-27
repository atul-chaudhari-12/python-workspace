class Sorting:
    def bubble_sort(self, array):
        for index in range(len(array) - 1):
            isSwapped = False
            for index2 in range(len(array) - 1 - index):
                if array[index2] > array[index2 + 1]:
                    isSwapped = True
                    array[index2], array[index2 + 1] = array[index2 + 1], array[index2]
            if not isSwapped:
                break
        return array

    def selection_sort(self, array):
        for index in range(len(array) - 1):
            indexOfSmallestNumber = index
            for index2 in range(index + 1, len(array)):
                if array[index2] < array[indexOfSmallestNumber]:
                    indexOfSmallestNumber = index2
            if indexOfSmallestNumber != index:
                array[index], array[indexOfSmallestNumber] = (
                    array[indexOfSmallestNumber],
                    array[index],
                )
        return array
        
    def quick_sort_list_using_comprehension(self, array):
        if len(array) <= 1:
            return array
        pivote = array[0]
        left = [x for x in array[1:] if x < pivote]
        right = [y for y in array[1:] if y > pivote]
        return self.quick_sort_list_using_comprehension(left) + [pivote] + self.quick_sort_list_using_comprehension(right)

    def quick_sort(self, array, left, right):
        if left < right:
            position = self.partition(array, left, right)
            self.quick_sort(array, left, position-1)
            self.quick_sort(array, position + 1, right)
        return array
    
    def partition(self, array, left, right):
        pivote=array[right]
        i = left
        j = right-1
        while i < j:
            while i < right and array[i] < pivote:
                i += 1
            while j > left and array[j] >= pivote:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]

        array[i], array[right] = array[right], array[i]

        return i    

if __name__ == "__main__":
    obj = Sorting()
    print("===========================Bubble Sort ===================")
    print (obj.bubble_sort([1,2,3,4,5,6,7,8,9]))
    print (obj.bubble_sort([9,8,7,6,5,4,3,2,1]))
    print (obj.bubble_sort([4,7,3,7,4,5,79,1,5,3,6,8,0]))
    print("====================Selection Sort===================")
    print (obj.selection_sort([1,2,3,4,5,6,7,8,9]))
    print (obj.selection_sort([9,8,7,6,5,4,3,2,1]))
    print (obj.selection_sort([4,7,3,7,4,5,79,1,5,3,6,8,0]))
    print ("=================== Quick Sort Using List Comprehension =======================")
    print (obj.quick_sort_list_using_comprehension([1,2,3,4,5,6,7,8,9]))
    print (obj.quick_sort_list_using_comprehension([9,8,7,6,5,4,3,2,1]))
    print (obj.quick_sort_list_using_comprehension([4,7,3,7,4,5,79,1,5,3,6,8,0]))
    print ("=================== Quick Sort Using Partition =======================")
    print (obj.quick_sort([1,2,3,4,5,6,7,8,9], 0, 8))
    print (obj.quick_sort([9,8,7,6,5,4,3,2,1], 0, 8))
    print (obj.quick_sort([4,7,3,7,4,5,79,1,5,3,6,8,0], 0, 12))