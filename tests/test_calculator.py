from tdd.tdd import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    def test_operation(self):
        num1 = 4
        num2 = 5

        calc = Calculator(num1, num2)

        operations = {
            '+': calc.add(),
            '-': calc.subtract(),
            '*': calc.multiply(),
        }

        try:
            op = input("Enter operation (+, -, *): ")
            if op not in operations:
                raise ValueError
        except ValueError:
            print("Invalid operation!")
        else:
            if op == '+':
                self.assertEqual(calc.add(), 9)
            elif op == '-':
                self.assertEqual(calc.subtract(), -1)
            elif op == '*':
                self.assertEqual(calc.multiply(), 20)


if __name__ == "__main__":
    unittest.main()
