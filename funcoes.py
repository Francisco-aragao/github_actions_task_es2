
class Calculator:

    def add(self, num1: int, num2):

        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError("Both numbers must be integers")

        return num1 + num2

    def subtract(self, num1, num2):

        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError("Both numbers must be integers")
        
        return num1 - num2

    def multiply(self, num1, num2):

        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError("Both numbers must be integers")
        
        return num1 * num2

    def divide(self, num1, num2):
        
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError("Both numbers must be integers")
        
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return num1 / num2

    def concat(self, str1, str2):

        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError("Both inputs must be strings")
        
        return str1 + str2

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(2, 3))
    print(calc.concat("hello", "world"))