def is_palindrom(s: str):
    s = s.replace(" ", "")
    s = s.lower()
    palindrom_flag = True
    for n in range(len(s)//2):
        if s[n] != s[len(s)-n-1]:
            palindrom_flag = False
    return palindrom_flag

print(is_palindrom("Kobyła ma mały bok"))
