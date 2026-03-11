from decorators import time_decorator


@time_decorator('sorting', 'insertion_sort')
def insertion_sort(elements: list | str) -> list:
    length = len(elements)

    if type(elements) == str:
        elements = list(elements)

    for i in range(1, length):
        j = i
        while j > 0 and elements[j] < elements[j - 1]:
            elements[j], elements[j - 1] = elements[j - 1], elements[j]
            j -= 1

    return elements


if __name__ == "__main__":
    array = [1, 2, 3, 14, 5, 78]
    string_array = 'selectionsort'

    print(insertion_sort(string_array))
    print(insertion_sort(array))
