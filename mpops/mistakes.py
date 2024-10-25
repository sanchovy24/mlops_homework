def add_numbers(a, b):
    return a + b

def main():
    result = add_numbers(5, '10')  # Ошибка: сложение int и str
    print("The result is: " + result)  # Ошибка: конкатенация str и int

if __name__ == "__main__":
    main()