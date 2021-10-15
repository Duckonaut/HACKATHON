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
