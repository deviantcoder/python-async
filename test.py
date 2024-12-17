def find_word(file, word):
    g_index = 0
    for line in file:
        index = 0

        while index != -1:
            index = line.find(word, index)

            if index > -1:
                yield g_index + index
                index += 1

        g_index += len(line)



try:
    with open('test.txt') as file:
        a = find_word(file, 'Lorem')
        print(list(a))
except FileNotFoundError:
    print('no file was found')
