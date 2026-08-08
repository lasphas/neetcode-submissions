class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        premap = {i:[] for i in range(numCourses)}

        for csr,pre in prerequisites:
            premap[csr].append(pre)
            
        visit = set()

        def dfs(csr):
            if csr in visit :
                return False
            if premap[csr] == []:
                return True

            visit.add(csr)

            for pre in premap[csr]:
                if not dfs(pre) :
                    return False
            visit.remove(csr)
            premap[csr] = []
            return True

        for courses in range(numCourses):
            if not dfs(courses):
                return False
        return True