from decorators import time_decorator


@time_decorator('sorting', 'selection_sort')
def selection_sort(elements: list | str) -> list:
    length = len(elements)

    if type(elements) == str:
        elements = list(elements)

    for i in range(length):
        min_element_number = i
        for j in range(i + 1, length):
            if elements[j] < elements[min_element_number]:
                min_element_number = j

        elements[i], elements[min_element_number] = elements[min_element_number], elements[i]

    return elements


if __name__ == "__main__":
    array = [1, 2, 3, 14, 5, 78]
    string_array = 'selectionsort'

    print(selection_sort(string_array))
    print(selection_sort(array))
