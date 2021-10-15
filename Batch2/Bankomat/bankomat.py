from typing import List


def divideIntoNotes(value: int, noteValues: List[int]):
    
    for i, v in enumerate(reversed(noteValues)):
        count = value // v
        if count > 0:
            print(f'{v} x{count}')

            value = value % v

        if value == 0:
            break

def main():
    noteValueCount = int(input())
    noteValues = [int(input()) for i in range(noteValueCount)]

    valueToDivideCount = int(input())
    valuesToDivide = [int(input()) for i in range(valueToDivideCount)]

    for v in valuesToDivide:
        print(f'\n{v}:')
        divideIntoNotes(v, noteValues)

if __name__ == '__main__':
    main()