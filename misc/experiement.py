def common(word_count, num):
    new_dict = {}
    for word in word_count:
        if word_count[word] not in new_dict:
            new_dict[word_count[word]] = [word]
        else:
            new_dict[word_count[word]] += [word]

    lst = []

    for count in new_dict:
        lst.append((count, new_dict[count]))
    lst.sort(reverse=True)
    new = []
    for i in range(num):
        if i < len(lst):
            if len(lst[i][1]) == 1:
                new.append(lst[i])

    word_count.clear()
    for tuple_ in new:
        word_count[tuple_[1][0]] = tuple_[0]
