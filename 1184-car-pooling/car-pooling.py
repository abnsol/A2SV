class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # range sum query
        queries = [0] * 1001

        for nump,fromi,to in trips:
            queries[fromi] += nump
            if to != 1000:
                queries[to] -= nump
        
        for i in range(1,1001):
            queries[i] += queries[i - 1]
        
        print(queries)
        for i in range(1,1001):
            if queries[i] > capacity or queries[i - 1] > capacity:
                return False
        
        return True