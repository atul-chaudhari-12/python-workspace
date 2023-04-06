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
