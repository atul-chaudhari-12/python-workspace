"""
This File contains solution to a few fibonacci releated coding questions
"""

class FibonacciSeriesPlaygroundClass():

    # 1. Infinite fibonnaci series using gnererators
    def fibonacciGeneratorUsingPythonGenerator(self):
        first_number = 0
        second_number = 1
        while True:
            yield second_number
            first_number, second_number = second_number, first_number+second_number
    
    #2. Fibonacci series using recursion
    def fibonacciSeriesUsingRecursion(self, number):
        if number<=1:
            return number        
        return self.fibonacciSeriesUsingRecursion(number-1) + self.fibonacciSeriesUsingRecursion(number-2)

if __name__=="__main__":
    obj = FibonacciSeriesPlaygroundClass()
    infiniteFibonacciGenerator = obj.fibonacciGeneratorUsingPythonGenerator()
    print(next(infiniteFibonacciGenerator))
    print(next(infiniteFibonacciGenerator))
    print(next(infiniteFibonacciGenerator))
    print(next(infiniteFibonacciGenerator))
    print(next(infiniteFibonacciGenerator))
    print(next(infiniteFibonacciGenerator))
    print("===============================================")    
    for i in range(10):
        print(obj.fibonacciSeriesUsingRecursion(i))
