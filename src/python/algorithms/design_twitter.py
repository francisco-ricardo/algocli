"""
355. Design Twitter
https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets, 
follow/unfollow other users, and get the 10 most recent tweets in the user's 
news feed.

Implement the Twitter class:

- Twitter() Initializes the Twitter object.
- void postTweet(int userId, int tweetId) Posts a new tweet with ID tweetId by 
the user userId. Each call to this function will be made with a unique tweetId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs
from the userId's news feed. Each item in the news feed must be posted by users
following the userId. Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId
    follows the user with ID followeeId. If the operation is invalid, it should
    be a no-op.
- void unfollow(int followerId, int followeeId) The user with ID followerId
    unfollows the user with ID followeeId. If the operation is invalid, it should
    be a no-op.
- The user will never follow themselves.
- The tweetId and userId are positive integers, and the followeeId will be 
    different from followerId.
- The tweetId and userId are less than or equal to 10^4.
- The maximum number of tweets will not exceed 10^4.
- The maximum number of users will not exceed 200.
- The maximum number of function calls will be 2000.
- The tweets will be posted in chronological order.
""" 

from collections import defaultdict
from typing import List
from itertools import count


class Twitter:

    def __init__(self):
        """
        Initializes the Twitter object.
        """
        self.tweets = defaultdict(list)  # userId -> list of tweets
        self.followees = defaultdict(set)  # userId -> set of followees
        self.time = count()  # to keep track of tweet order


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Posts a new tweet with ID tweetId by the user userId.
        Each call to this function will be made with a unique tweetId.

        The tweet is stored as a tuple of (timestamp, tweetId)
        to maintain the order of tweets.
        The timestamp is generated using the count() iterator.
        This ensures that each tweet has a unique timestamp.        
        """
        self.tweets[userId].append((next(self.time), tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieves the 10 most recent tweet IDs from the userId's news feed.
        Each item in the news feed must be posted by users following the userId.
        Tweets must be ordered from most recent to least recent.
        """
        # Get the tweets of the user and their followees
        tweets = []
        for followee in self.followees[userId]:
            tweets.extend(self.tweets[followee])
        tweets.extend(self.tweets[userId])

        # Sort the tweets by timestamp in descending order
        tweets.sort(reverse=True)

        # Return the 10 most recent tweet IDs
        return [tweetId for _, tweetId in tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId follows the user with ID followeeId.
        If the operation is invalid, it should be a no-op.

        Add the followeeId to the set of followees for followerId
        This ensures that the followerId does not follow themselves.        
        """
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)
              
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId unfollows the user with ID followeeId.
        If the operation is invalid, it should be a no-op.

        Remove the followeeId from the set of followees for followerId
        This ensures that the followerId does not unfollow themselves.        
        """
        if followerId != followeeId:
            self.followees[followerId].discard(followeeId)
            


# Example usage:    
if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # Output: [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # Output: [6, 5]
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))  # Output: [5]
