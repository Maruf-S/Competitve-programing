class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)-1
        mem = [[-1]*(4) for i in range(n+1)]
        def jumps(pos, lane):
            # if we reached the last position return 0
            if pos == n:  
                return 0
            # first we check in memoization table, if already present return that
            if mem[pos][lane]!=-1: 
                return mem[pos][lane]
            #if either we dont have any obstacle in next pos or the obstacle in not in our lane, then 
            # recur for the next position but in the same lane
            if obstacles[pos+1] == 0 or obstacles[pos+1]!=lane: 
                mem[pos][lane] =  jumps(pos+1, lane)
                return mem[pos][lane]
            # if obstacle is in our lane then we need to jump to sideways
            if obstacles[pos+1] == lane:
                first, second = sys.maxsize, sys.maxsize
                # we can check for all the lanes, if currently in lane 1, then check for lane 2 and 3
                if lane == 1:
                    #if we have a obstacle in 2, then we cant jump there.
                    #else we can jump so add 1 to the ans and recur for next position
                    if obstacles[pos]!=2:
                        first = 1+ jumps(pos+1, 2)
                    if obstacles[pos]!=3:
                        second =1+ jumps(pos+1, 3)
                if lane == 2:
                    if obstacles[pos]!=1:
                        first = 1+ jumps(pos+1, 1)
                    if obstacles[pos]!=3:
                        second = 1+ jumps(pos+1, 3)
                if lane == 3:
                    if obstacles[pos]!=2:
                        first = 1+ jumps(pos+1, 2)
                    if obstacles[pos]!=1:
                        second = 1+ jumps(pos+1, 1)
                #after calculation of first and second path, take the minimum
                mem[pos][lane] =  min(first, second)
                return mem[pos][lane]
        return jumps(0, 2)