from decorators import time_decorator


@time_decorator('string', 'substring_in_string', version=1)
def substring_in_string_version_1(string: str, substring: str) -> int | bool:
    string_len, substring_len = len(string), len(substring)

    if substring_len > string_len:
        return False

    for i in range(string_len - substring_len + 1):
        j = 0
        while j < substring_len and string[i + j] == substring[j]:
            j += 1

        if j == substring_len:
            return i

    return False


@time_decorator('string', 'substring_in_string', version=2)
def substring_in_string_version_2(string: str, substring: str) -> int | bool:
    string_len, substring_len = len(string), len(substring)

    if substring_len > string_len:
        return False

    for i in range(string_len - substring_len + 1):
        if string[i:i + substring_len] == substring:
            return i

    return False


if __name__ == "__main__":
    text = 'asdfgfdsa'
    sub = 'dsajneenrgreng'

    print(substring_in_string_version_1(text, sub))
    print(substring_in_string_version_2(text, sub))
