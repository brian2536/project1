def add_subtract(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

if __name__ == "__main__":
    try:
        a = int(input("첫 번째 숫자를 입력하세요: "))
        b = int(input("두 번째 숫자를 입력하세요: "))
        addition, subtraction = add_subtract(a, b)
        print(f"덧셈 결과는 {a}와 {b}의 합입니다: {add}")
        print(f"{a} - {b} = {subtraction}")
    except ValueError:
        print("유효한 정수를 입력하세요.")

def add_subtract_multiply_divide(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "나눗셈 불가"
    return addition, subtraction, multiplication, division

if __name__ == "__main__":
    try:
        a = int(input("첫 번째 숫자를 입력하세요: "))
        b = int(input("두 번째 숫자를 입력하세요: "))
        add, sub, mul, div = add_subtract_multiply_divide(a, b)
        print(f"{a} + {b} = {add}")
        print(f"{a} - {b} = {sub}")
        print(f"{a} * {b} = {mul}")
        print(f"{a} / {b} = {div}")
    except ValueError:
        print("유효한 정수를 입력하세요.")
