def main():
    object_list = []
    with open(__file__, 'r') as itself:
        content = itself.readlines()
        edit = content[1][:-1]
        itself.close()
    
    content.pop(1)

    st_half = list(edit)[:18].copy()
    nd_half = list(edit)[18:].copy()

    dct = {
        0: '\'Pierwiastek Geniuszu\'',
        1: '\'jest\'',
        2: '\'Najlepszy\''
        }

    nd_half.insert(len(nd_half)-1, dct[len(object_list) % 3]+ ', ')
    nd_half.append('\n')

    content.insert(1, "".join(st_half+nd_half))
    print("".join(nd_half[:-1]))

    with open(__file__, 'w') as itself:
        itself.write("".join(content))
        itself.close()

if __name__ == "__main__":
    main()
