class Twitter:

    def __init__(self):
        self.count = 0
        self.users = defaultdict(list) # user: [(count, tweet)]
        self.follows = defaultdict(set) # user: [followees]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.users[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []
        # add most recent own tweet to heap
        if userId in self.users:
            index = len(self.users[userId]) - 1
            cnt, tweet = self.users[userId][index]
            heap.append((cnt, tweet, userId, index - 1))

        # add most recent tweet of every followee
        for followeeId in self.follows[userId]:
            if followeeId in self.users:
                index = len(self.users[followeeId]) - 1
                cnt, tweet = self.users[followeeId][index]
                heap.append((cnt, tweet, followeeId, index - 1))
        
        heapq.heapify_max(heap)

        while heap and len(feed) < 10:
            cnt, tweet, id, newIndex = heapq.heappop_max(heap)
            feed.append(tweet)
            if newIndex >= 0:
                newCnt, newTweet = self.users[id][newIndex]
                heapq.heappush_max(heap, (newCnt, newTweet, id, newIndex - 1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.follows[followerId]:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
