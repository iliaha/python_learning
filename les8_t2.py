class Division:

    @staticmethod
    def division(num1, num2):
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            return 'На ноль делить нельзя!!!'
        except TypeError:
            return 'Работать только с числами!'


div = Division()
print(div.division(2, 2))
