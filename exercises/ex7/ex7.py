"""CSC148 Exercise 7: Recursion Wrap-Up

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains starter code for Exercise 7.
"""


##############################################################################
# Task 1: A variation on sorting
##############################################################################
def kth_smallest(lst, k):
    """Return the <k>-th smallest element in <lst>.

    Raise IndexError if k < 0 or k >= len(lst).
    Note: for convenience, k starts at 0, so kth_smallest(lst, 0) == min(lst).

    Precondition: <lst> does not contain duplicates.

    @type lst: list[int]
    @type k: int
    @rtype: int
    >>> lst = [0,1,2,3,4,5]
    >>> kth_smallest(lst, 5)
    5
    >>> kth_smallest(lst, 0)
    0
    >>> lst2 = [1,4,2,6,7,8,12,9]
    >>> kth_smallest(lst2, 3)
    6
    >>> kth_smallest(lst2, 6)
    9
    >>> kth_smallest(lst2, 7)
    12
    """
    # Hint: partition the list based on a chosen pivot.
    # smaller, bigger = partition(...)
    # Check the length of <smaller>, and use that to figure out which list
    # to recurse on. You only need to recurse on one!
    if lst == []:
        pass
    pivot = lst[0]
    smaller, bigger = partition(lst, pivot)

    if k < 0 or k >= len(lst):
        raise IndexError
    elif k == len(smaller) - 1:
        return pivot
    elif k > len(smaller) - 1:
        return kth_smallest(bigger, k - len(smaller))
    else:
        smaller.remove(pivot)
        return kth_smallest(smaller, k)


def partition(lst, pivot):
    """Return a partition of <lst> according to pivot.

    Return two lists, where the first is the items in <lst>
    that are <= pivot, and the second is the items in <lst>
    that are > pivot.

    @type lst: list
    @type pivot: object
    @rtype: (list, list)
    """
    # Use a loop to go through <lst> to build up the two
    # lists. Note that <smaller> and <bigger> do *not* need to be sorted here.
    smaller = []
    bigger = []

    for i in lst:
        if i <= pivot:
            smaller.append(i)
        else:
            bigger.append(i)
    return smaller, bigger


##############################################################################
# Task 2: Something a little different
##############################################################################
# The file of English words to use. The one we've provided doesn't contain
# plural forms. Assume this list is in alphabetical order.
FILE = 'dict.txt'
LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def anagrams(phrase):
    """Return a list of all anagrams of <phrase>.

    The anagrams are returned in alphabetical order.

    @type phrase: str
    @rtype: list[str]
    """
    # variables. This is particularly useful to see how the letter frequencies
    # are being represented.
    words = _generate_word_list()
    letter_count = _generate_letter_count(phrase.lower())
    return _anagrams_helper(words, letter_count)


def _generate_word_list():
    """Read in English words from <FILE> and return them.

    The returned list is in alphabetical order.

    @rtype: list[str]
    """
    words = []
    with open(FILE) as f:
        for line in f.readlines():
            words.append(line.strip().lower())
    return words


def _generate_letter_count(phrase):
    """Return a dictionary counting the letter occurrences in <string>.

    All letters in <phrase> are converted to lower-case.
    The keys in the returned dictionary are the 26 lower-case letters,
    'a', 'b', 'c', etc.

    Precondition: <phrase> contains only letters.

    @type phrase: str
    @rtype: dict[str, int]
    """
    lower = phrase.lower()
    letter_count = {}
    for char in LETTERS:
        letter_count[char] = lower.count(char)
    return letter_count


def _anagrams_helper(words, letter_count):
    """Return all the anagrams using the given letters and allowed words.

    Each anagram must use all the letters, with correct occurrences, given by
    <letter_count>, and must use only the words appearing in <words>.

    Note: we're using a helper function here so that you don't need to
    recompute <words> for each recursive call.

    The anagrams are returned in alphabetical order.

    Preconditions:
    - letter_count has 26 keys (one per lowercase letter),
      and each value is a non-negative integer.

    @type words: list[str]
    @type letter_count: dict[str, int]
    @rtype: list[str]
    """
    anagrams_list = []

    # 1. Base case - no more letters in <letter_count>.
    # In this case, there is only one valid anagram: the empty string.
    if sum(letter_count.values()) == 0:
        return ['']

    for word in words:
        # 2. For each word, check whether it can be used with the given
        # letter count. (If not, go onto the next word.)

        if not _within_letter_count(word, letter_count):
            continue

        # 3. If the word can be used, recurse and create anagrams.
        #  (i) Create a new dictionary that has the same values as letter_count,
        #      except with counts decreased based on the letters in <word>.
        #      Look at how we implemented _generate_letter_count for guidance.
        #  (ii) Call _anagrams_helper recursively with the new, reduced
        #       letter count.
        #  (iii) Combine <word> with the result of the recursive call to update
        #        <anagrams_list> with the anagrams that start with <word>.
        #        Don't forget to separate the words with a space.
        new = {}
        for char in LETTERS:
            new[char] = letter_count[char] - word.count(char)
        r = _anagrams_helper(words, new)
        if r == []:
            pass
        else:
            tmp = [word] + r
            tmp_str = ' '.join(tmp)
            if tmp_str[-1] == ' ':
                tmp_str = tmp_str[:len(tmp_str)-1]
            anagrams_list.append(tmp_str)

    # 4. Return the anagrams that can be made by the letters in letter_count.
    return anagrams_list


def flatten(lst):
    """Return a list containing all the str in <lst>.

    <lst> is a nested list, but the returned list should not be nested.
    The items should appear in the output in the left-to-right order they
    appear in <lst>.

    @type lst: str | list
    @rtype: list[str]
    """
    if isinstance(lst, str):
        return [lst]
    else:
        result = []
        for lst_i in lst:
            result += flatten(lst_i)
        return result


def _within_letter_count(word, letter_count):
    """Return whether <word> can be made using letters in <letter_count>."""
    for char in LETTERS:
        if word.count(char) > letter_count[char]:
            return False
    return True


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='pylintrc.txt')
