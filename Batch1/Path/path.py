from typing import List


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

def calculate_min(values):
    result = [None] * len(values)
    n = len(values) - 1
    for numbers in range(len(values[n])): 
        result[numbers] = values[n][numbers]

    for numbers in range(len(values)-2, -1, -1):
        for entry in range(len(values[numbers])):
            result[entry] = int(values[numbers][entry]) + min(int(result[entry]), int(result[entry+1]))
    
    return result[0]

def calculate_max(values):
    result = [None] * len(values)
    n = len(values) - 1
    for numbers in range(len(values[n])): 
        result[numbers] = values[n][numbers]

    for numbers in range(len(values)-2, -1, -1):
        for entry in range(len(values[numbers])):
            result[entry] = int(values[numbers][entry]) + max(int(result[entry]), int(result[entry+1]))
    
    return result[0]

def main():
    values = []
    with open("example.txt") as file_handle:
        for line in file_handle:
            t_list = get_data(line)
            values.append(t_list)
    min_result = calculate_min(values)
    max_result = calculate_max(values)
    print(min_result, max_result)

if __name__ == '__main__':
    main()
