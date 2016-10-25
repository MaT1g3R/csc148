set1 = """えいが			映画		movie
おんがく		音楽		music
ざっし			雑誌		magazine
スポーツ				sports
デート					date(romantic, not calendar)
テニス					tennis
テレビ					TV
アイスクリーム			icecream
あさごはん		朝ご飯		breakfast
おさけ			お酒		sake;alcohol
おちゃ			お茶		green tea
コーヒー				coffee
ばんごはん		晩ご飯		dinner
ハンバーガー				hamburger
ひるごはん		昼ご飯		lunch
みず			水		water
いえ			家		home; house
うち					home; house; my place
がっこう		学校		school
あさ			朝		morning
あした			明日		tomorrow
いつ					when
きょう			今日		today
～ごろ					at about..."""

set1_leftover = """music
school"""

set2 = """こんばん		今晩		tonight
しゅうまつ		週末		weekend
どようび		土曜日	Saturday
にちようび		日曜日	Sunday
まいにち		毎日		every day
まいばん		毎晩		every night
いく			行く		to go (destination に/へ)
かえる			帰る		to go back; to return (destination に/へ)
きく			聞く		to listen; to hear (～を)
のむ			飲む		to drink (～を)
はなす			話す		to speak; to talk (language を/で)
よむ			読む		to read (～を)
おきる			起きる		to get up
たべる			食べる		to eat (～を)
ねる			寝る		to sleep; to go to sleep"""

set2_left = """かえる			帰る		to go back; to return (destination に/へ)
はなす			話す		to speak; to talk (language を/で)"""

set1_2 = """えいが			映画		movie
おんがく		音楽		music
ざっし			雑誌		magazine
スポーツ				sports
デート					date(romantic, not calendar)
テニス					tennis
テレビ					TV
アイスクリーム			icecream
あさごはん		朝ご飯		breakfast
おさけ			お酒		sake;alcohol
おちゃ			お茶		green tea
コーヒー				coffee
ばんごはん		晩ご飯		dinner
ハンバーガー				hamburger
ひるごはん		昼ご飯		lunch
みず			水		water
いえ			家		home; house
うち					home; house; my place
がっこう		学校		school
あさ			朝		morning
あした			明日		tomorrow
いつ					when
きょう			今日		today
～ごろ					at about...
こんばん		今晩		tonight
しゅうまつ		週末		weekend
どようび		土曜日	Saturday
にちようび		日曜日	Sunday
まいにち		毎日		every day
まいばん		毎晩		every night
いく			行く		to go (destination に/へ)
かえる			帰る		to go back; to return (destination に/へ)
きく			聞く		to listen; to hear (～を)
のむ			飲む		to drink (～を)
はなす			話す		to speak; to talk (language を/で)
よむ			読む		to read (～を)
おきる			起きる		to get up
たべる			食べる		to eat (～を)
ねる			寝る		to sleep; to go to sleep"""

set1_2_left = """Saturday
かえる			帰る		to go back; to return (destination に/へ)"""

set3 = """みる			見る		to see; to look at; to watch (～を)
くる			来る		to come (destination に/へ)
する					to do (～を)
べんきょうする	勉強する	to study (～を)
いい					good
はやい			早い		early
あまり + negative			not much
ぜんぜん + negaive	全然		not at all
たいてい				usually
ちょっと				a little
ときどき		時々		sometimes
よく					often; much
そうですね				That’s right.; Let me see.
でも					but
どうですか				How about…?; How is…?
"""
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------


set1_2_3 = """えいが			映画		movie
おんがく		音楽		music
ざっし			雑誌		magazine
スポーツ				sports
デート					date(romantic, not calendar)
テニス					tennis
テレビ					TV
アイスクリーム			icecream
あさごはん		朝ご飯		breakfast
おさけ			お酒		sake;alcohol
おちゃ			お茶		green tea
コーヒー				coffee
ばんごはん		晩ご飯		dinner
ハンバーガー				hamburger
ひるごはん		昼ご飯		lunch
みず			水		water
いえ			家		home; house
うち					home; house; my place
がっこう		学校		school
あさ			朝		morning
あした			明日		tomorrow
いつ					when
きょう			今日		today
～ごろ					at about...
こんばん		今晩		tonight
しゅうまつ		週末		weekend
どようび		土曜日	Saturday
にちようび		日曜日	Sunday
まいにち		毎日		every day
まいばん		毎晩		every night
いく			行く		to go (destination に/へ)
かえる			帰る		to go back; to return (destination に/へ)
きく			聞く		to listen; to hear (～を)
のむ			飲む		to drink (～を)
はなす			話す		to speak; to talk (language を/で)
よむ			読む		to read (～を)
おきる			起きる		to get up
たべる			食べる		to eat (～を)
ねる			寝る		to sleep; to go to sleep
みる			見る		to see; to look at; to watch (～を)
くる			来る		to come (destination に/へ)
する					to do (～を)
べんきょうする	勉強する	to study (～を)
いい					good
はやい			早い		early
あまり + negative			not much
ぜんぜん + negaive	全然		not at all
たいてい				usually
ちょっと				a little
ときどき		時々		sometimes
よく					often; much
そうですね				That’s right.; Let me see.
でも					but
どうですか				How about…?; How is…?
"""
_alphatbet = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm;() .'


def remove(_input, alphabet):
    """
    @type _input: str
    @type alphabet: str
    @rtype: list[str]
    """
    _list = _input.split('\n')
    new_list = []
    for _str in _list:
        newstr = ''
        for _char in _str:
            if _char in alphabet:
                newstr += _char
        new_list.append(newstr)

    return new_list


def retain(_input, alphabet):
    """
    @type _input: str
    @type alphabet: str
    @rtype: list[str]
    """
    _list = _input.split('\n')
    new_list = []
    for _str in _list:
        newstr = ''
        for _char in _str:
            if _char not in alphabet:
                newstr += _char
        new_list.append(newstr)

    return new_list


def randomize(list_in):
    """
    @type list_in: list[str]
    @rtype: list[str]
    """
    from random import shuffle
    shuffle(list_in)
    return list_in

if __name__ == '__main__':

    removed = remove(set1_2, _alphatbet)
    shuffled = randomize(removed)
    for i in shuffled:
        print(i)

    counting = remove(set1_2_3, _alphatbet)
    print(len(counting))
