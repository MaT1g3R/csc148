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
names = ['Donald Trump:', 'Governor Gary Johnson:', 'Dr. Jill Stein:', 'Secretary Hillary Clinton:']


def _read_tweets_helper(file):
    lst = []
    with open(file) as f:
        for line in f:
            temp_line = line.strip('\n')
            lst.append(temp_line)
    return lst


def read_tweets(file, cand):
    """Each tweet end is marked by <<<EOT
    and each tweet begins with an info str
    then 1 or more text strs

    the raw file looks like:
    ['Trump:', 'info','text','text','<<<EOT', 'info','text','<<<EOT', 'Clinto:','info','text','text','<<<EOT', 'info','text','<<<EOT']
    So how the fuck do i format this shit
    """
    raw = _read_tweets_helper(file)

    curr_can = ''
    tmp_tweet = []

    for i in raw:
        if i in names:  # A new candidate
            curr_can = i.strip(':')
            cand[curr_can] = []  # initialize a new key
        else:  # this deals with the tweets under the cand
            if i != '<<<EOT':
                tmp_tweet.append(i)
            else:
                # do something here
                info_list = tmp_tweet[0].split(',')

                text = '\n'.join(tmp_tweet[1:])

                date = info_list[1]
                source = info_list[3]
                fav = info_list[4]
                retweet = info_list[5]

                formated = (curr_can, text, date, source, fav, retweet)

                cand[curr_can].append(formated)
                tmp_tweet = []
