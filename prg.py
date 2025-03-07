import numpy as np

def main():
    # Создание массива из 10 элементов (0–9)
    arr = np.arange(10)
    print("Исходный массив:", arr)

    # Вывод элементов массива с индексами от 3 до 6
    print("Элементы с индексами от 3 до 6:", arr[3:7])

    # Изменение значений элементов массива с индексами от 7 до 9
    arr[7:10] = [10, 20, 30]
    print("Измененный массив:", arr)

if __name__ == "__main__":
    main()
