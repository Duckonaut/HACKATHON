from typing import List

def read_values():
    values = []
    with open("example.txt") as file_handle:
        for line in file_handle:
            temp_list = list(line)
            t_list = [number for number in temp_list if number.isnumeric()]
            values.append(t_list)
    return values

def get_data(s: str) -> List[int]:
    lastSpace = False
    formatted = ''

    for c in s:
        if c == ' ' and not lastSpace:
            formatted += ' '
            lastSpace = True
        elif c.isnumeric():
            formatted += c
            lastSpace = False

    return [int(n) for n in formatted.split(' ')]

def calculate_min(values, result, n):
    for numbers in range(len(values[n])): 
        result[numbers] = values[n][numbers]
    numbers = len(values) - 2
    while numbers >= 0:
        for entry in range(len(values[numbers])):
            result[entry] = int(values[numbers][entry]) + min(result[entry], result[entry+1])
        numbers -= 1
    
    return result[0]

def calculate_max(values, result, n):
    for numbers in range(len(values[n])): 
        result[numbers] = values[n][numbers]
    numbers = len(values) - 2
    while numbers >= 0:
        for entry in range(len(values[numbers])):
            result[entry] = int(values[numbers][entry]) + max(result[entry], result[entry+1])
        numbers -= 1
    return result[0]

def main():
    values = read_values()
    values = []
    with open("example.txt") as file_handle:
        for line in file_handle:
            t_list = get_data(line)
            values.append(t_list)
    r = [None] * len(values)
    n = len(values) - 1
    min_result = calculate_min(values, r, n)
    max_result = calculate_max(values, r, n)
    print(min_result, max_result)

if __name__ == '__main__':
    main()
