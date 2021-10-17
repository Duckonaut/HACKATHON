days = { 
    'poniedzialek': 0, 
    'wtorek': 1, 
    'sroda': 2, 
    'czwartek': 3, 
    'piatek': 4, 
    'sobota': 5,
    'niedziela': 6, 
}

def main():
    line = input().strip().split(' ')
    day = line[0]
    offset = int(line[1])

    
    print(list(days.keys())[(days[day] + offset) % 7])

if __name__ == '__main__':
    main()