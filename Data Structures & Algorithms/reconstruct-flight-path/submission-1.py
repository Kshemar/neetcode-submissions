class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for src, dest in sorted(tickets, reverse=True):
            adj[src].append(dest)

        res = []
        def dfs(src):
            while adj[src]:
                v = adj[src].pop()
                dfs(v)
            res.append(src)

        dfs("JFK")
        return res[::-1]