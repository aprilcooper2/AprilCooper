#There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.
#Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        f = collections.defaultdict(dict)
        for flight in flights:
            f[flight[0]][flight[1]] = flight[2]
        pq = [(0, src, K)]
        while pq:
            price, city, k = heapq.heappop(pq)
            if city == dst:
                return price
            if k >= 0:
                for route in f[city]:
                    heapq.heappush(pq, (price + f[city][route], route, k - 1))
        return -1
