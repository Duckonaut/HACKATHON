from typing import List, Tuple


def getPossibleDiamonds(newPos: Tuple[int, int], diamonds: List[Tuple[int, int]]) -> int:
    return len([d for d in diamonds if d[0] >= newPos[0] and d[1] >= newPos[1]])

def main():
    size = input().split()
    size = (int(size[0]), int(size[1]))

    diamondNumber = int(input())

    diamonds = []
    for _ in range(diamondNumber):
        point = input().split()
        point = (int(point[0]), int(point[1]))

        diamonds.append(point)
    
    position = (0, 0)
    path = ''
    total = 0

    while position[0] != size[0] - 1 or position[1] != size[1] - 1:
        if position[0] == size[0] - 1:
            position = (position[0], position[1] + 1)
            path += 'D'

        elif position[1] == size[1] - 1:
            position = (position[0] + 1, position[1])
            path += 'P'

        else:
            if getPossibleDiamonds((position[0] + 1, position[1]), diamonds) > getPossibleDiamonds((position[0], position[1] + 1), diamonds):
                position = (position[0] + 1, position[1])
                path += 'P'
            else:
                position = (position[0], position[1] + 1)
                path += 'D'

        if position in diamonds:
            total += 1
    
    print(total)
    print(path)


if __name__ == '__main__':
    main()