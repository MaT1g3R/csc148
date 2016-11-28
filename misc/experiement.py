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

candidates = {}

def _read_tweets_helper(file):
    lst = []
    with open(file) as f:
        for line in f:
            temp_line = line.strip('\n')
            lst.append(temp_line)

    new_lst = []

    tmp = []
    tmp_tweet = []

    for i in lst:
        if i[-1] == ':':
            if tmp != []:
                new_lst.append(tmp)
            tmp = []
            tmp_tweet = []
            tmp.append(i[:-1])

        elif i != '<<<EOT':
            tmp_tweet.append(i)

        elif i == '<<<EOT':
            tmp.append(tmp_tweet)
            tmp_tweet = []

    return new_lst


def read_tweets(file, _candidates):
    lst = _read_tweets_helper(file)
    for i in lst:
        _candidates[i[0]] = []
        for ele in i[1:]:
            info_list = ele[0].split(',')
            tweet = '\n'.join(ele[1:])
            info_and_tweet_list = [i[0]] + [tweet] + [info_list[1]] + [info_list[3]] + [info_list[4]] + [info_list[5]]
            tmp_tuple = tuple(info_and_tweet_list)
            _candidates[i[0]].append(tmp_tuple)


read_tweets('short_data.txt', candidates)
print(candidates)
