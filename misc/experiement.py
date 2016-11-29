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
    for line in file:
        temp_line = line.strip('\n')
        lst.append(temp_line)
    return lst


def read_tweets(file):
    """Each tweet end is marked by <<<EOT
    and each tweet begins with an info str
    then 1 or more text strs

    the raw file looks like:
    ['Trump:', 'info','text','text','<<<EOT', 'info','text','<<<EOT', 'Clinto:','info','text','text','<<<EOT', 'info','text','<<<EOT']
    So how the fuck do i format this shit
    """
    cand = {}
    raw = _read_tweets_helper(file)
    past_cands = []
    curr_can = ''
    tmp_tweet = []

    for i in raw:
        if i in names and i not in past_cands:  # A new candidate
            _id = raw.index(i) - 1
            tmp_line = []
            try:
                tmp_line.append(raw[_id])
            finally:
                tmp_line.append(None)

            if tmp_line[0] == '<<<EOT' or tmp_line[0] is None:
                past_cands.append(i)
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

    return cand


def most_popular(info, start, end):

    cand = {}

    for key in info:
        cand[key] = 0

    for key, val in info.items():  # val is a list of tuples
        for tup in val:

            name = tup[0]
            date = int(tup[2])
            fav = int(tup[4])
            ret = int(tup[5])

            if start <= date <= end:
                cand[name] += fav + ret

    max_num = cand[max(cand)]
    most = []

    for key, val in cand.items():
        if val == max_num:
            most.append(key)

    return most[0] if len(most) == 1 else 'tie'

