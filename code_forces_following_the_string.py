basic = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

num_outputs = int(input())


def find_index_of_first(index_list, what):
    return index_list.index(what)


for i in range(num_outputs):
    len_word = int(input())
    word = list(map(int, input().split()))
    track = [0] * 26
    unique = 0
    string = ""
    for number in word:
        if number == 0:
            string += basic[unique]
            track[unique] += 1
            unique += 1
        else:
            where = find_index_of_first(track, number)
            track[where] += 1
            string += basic[where]
    print(string)
