class SortArray:
    def __init__(self, array = []):
        self.array = array
    

    def SelectionSort(self):
        for i in range(0, len(self.array)):
            for j in range (i + 1, len(self.array)):
                if self.array[i] > self.array[j]:
                    # temp = self.array[i]
                    # self.array[i] = self.array[j]
                    # self.array[j] = temp
                    self.array[i], self.array[j] = self.array[j], self.array[i]
        print("Selection sort")
        return self.array
    def BubbleSort(self):
        for i in range (0, len(self.array)):
            for j in range (0, len(self.array) - i - 1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        print("Bubble sort")
        return self.array
    
    def InsertionSort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
        print("Insertion sort")
        return self.array


array_selection = [312,12345,123412,1231740,9568,8473,28936428,2871,9753,362351]
selection_sort = SortArray(array_selection)
print(selection_sort.SelectionSort())

array_bubble = [31272, 123871, 9238, 3162,83712,127884,1237,9732,84673,6534,12,4286732]
bubble_sort = SortArray(array_bubble)
print(bubble_sort.BubbleSort())

array_insertion = [123,41234,5232135,121,3,41234123,4123154123,5887,8,7567,856756,85,7568,567,5342]
insertion_sort = SortArray(array_insertion)
print(insertion_sort.InsertionSort())