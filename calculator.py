class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        if a < 0 and b <0:
            return a - b
        
        if a <0 or b<0:
            if a<0:
                return -(abs(a)+b)
            elif b<0:
                return (a+abs(b))
            
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)+1):
            result = self.add(result, i)

        if a < 0 and b <0:
            return result

        elif a < 0 or b <0:
            return -result
        
        return result

    def divide(self, a, b):
        result = 0
        og_a =a
        while abs(a) >= abs(b):
            a = self.subtract(abs(a), abs(b))
            result += 1

        if og_a < 0 and b < 0:
            return result
        
        if og_a < 0 or b < 0:
            return -result
        
        return result

    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(-2, -2))
    print("Example: subtraction: ", calc.subtract(-7,2))
    print("Example: subtraction: ", calc.subtract(7,-2))
    print("Example: subtraction: ", calc.subtract(7,2))
    print("Example: subtraction: ", calc.subtract(-7,-2))
    print("Example: multiplication: ", calc.multiply(-2, -3))
    print("Example: multiplication: ", calc.multiply(2, -3))
    print("Example: multiplication: ", calc.multiply(-2, 3))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(-10, 2))
    print("Example: division: ", calc.divide(10, -2))
    print("Example: division: ", calc.divide(-10, -2))
    print("Example: division: ", calc.divide(10,2))
    print("Example: division: ", calc.divide(2,10))
    print("Example: modulo: ", calc.modulo(10, 3))
    print("Example: modulo: ", calc.modulo(10, 10))