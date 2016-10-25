"""tweet class intro"""

from datetime import *

class Tweet:
    """A tweet, like in twitter

    Elaboration like...

    === Attrinute ===
    @type content: str
        The content of the tweet
    @type user_id: str
        The id of the uer who wrote this tweet
    @type created_at: str
        The date the tweet was written
    @type likes: int
        The number of likes this tweet has recived
    """

    def __init__(self,who,what,when):
        """Initialze a new tweet

        @type self: Tweet
        @type who: str
        @type what: str
        @type when: str
        @rtype: None
        """

        self.user_id = who
        self.content = what
        self.created_at = when
        self.likes = 0

    def like(self,n):
        """
        write doc strings
        """
        self.likes += n

def retweet(new_user, tweet, new_date):
    return Tweet(new_user , tweet.content , new_date)



class User:
    """ A Twitter user




    """
