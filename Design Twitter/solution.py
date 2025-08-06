import heapq as hq
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetsMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsMap[userId].append((self.count, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        print(f"self.followMap[userId]: {self.followMap[userId]}")
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            print(f"self.tweetsMap[followee]: {self.tweetsMap[followee]}")
            tweet_count = 0
            for i in range(len(self.tweetsMap[followee])-1,-1,-1):
                print(f"adding tqeet to pq")
                if tweet_count >= 10:
                    print(f"broke out")
                    break
                print(f"adding tqeet to pq: {self.tweetsMap[followee][i]}")
                hq.heappush(pq, self.tweetsMap[followee][i])
                tweet_count += 1
        
        print(f"pq: {pq}")
        pop_count = 0
        res = []
        while len(pq) > 0 and pop_count < 10:
            print(f"in while res: {res}")
            val = hq.heappop(pq)
            print(f"val: {val}")
            res.append(val[1])
            pop_count += 1
        print(f"out while res: {res}")
        return res

    # def getNewsFeed(self, userId: int) -> List[int]:
    #     res = []
    #     minHeap = []

    #     self.followMap[userId].add(userId)
    #     for followeeId in self.followMap[userId]:
    #         if followeeId in self.tweetsMap:
    #             index = len(self.tweetsMap[followeeId]) - 1
    #             count, tweetId = self.tweetsMap[followeeId][index]
    #             heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

    #     while minHeap and len(res) < 10:
    #         count, tweetId, followeeId, index = heapq.heappop(minHeap)
    #         res.append(tweetId)
    #         if index >= 0:
    #             count, tweetId = self.tweetsMap[followeeId][index]
    #             heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
    #     return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)