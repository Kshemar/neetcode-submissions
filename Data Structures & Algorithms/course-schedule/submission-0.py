class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visit = set()
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            cycle.remove(course)
            visit.add(course)

            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
