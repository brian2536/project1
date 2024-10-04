def add_subtract(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

if __name__ == "__main__":
    try:
        a = int(input("첫 번째 숫자를 입력하세요: "))
        b = int(input("두 번째 숫자를 입력하세요: "))
        addition, subtraction = add_subtract(a, b)
        print(f"{a} + {b} = {addition}")
        print(f"{a} - {b} = {subtraction}")
    except ValueError:
        print("유효한 정수를 입력하세요.")
