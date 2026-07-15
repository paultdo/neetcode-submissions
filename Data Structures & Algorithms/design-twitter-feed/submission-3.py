class Twitter:

    def __init__(self):
        self.count = 0
        self.users = defaultdict(list) # user: [(count, tweet)]
        self.follows = defaultdict(list) # user: [followees]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.users[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []
        for i in range(len(self.users[userId])):
            heap.append(self.users[userId][i])
        
        for i in range(len(self.follows[userId])):
            for j in range(len(self.users[self.follows[userId][i]])):
                heap.append(self.users[self.follows[userId][i]][j])
        
        heapq.heapify_max(heap)

        i = 0
        while i < 10 and heap:
            feed.append(heapq.heappop_max(heap)[1])
            i += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
