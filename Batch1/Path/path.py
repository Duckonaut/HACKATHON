def read_values():
    values = []
    with open("example.txt") as file_handle:
        for line in file_handle:
            temp_list = list(line)
            t_list = [number for number in temp_list if number.isnumeric()]
            values.append(t_list)
    return values

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
    values = read_values()
    min_result = calculate_min(values)
    max_result = calculate_max(values)
    print(min_result, max_result)
