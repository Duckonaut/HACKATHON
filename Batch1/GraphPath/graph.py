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

def main():
    values = []
    with open("example.txt") as file_handle:
        for line in file_handle:
            t_list = get_data(line)
            values.append(t_list)
    print(values)

if __name__ == '__main__':
    main()