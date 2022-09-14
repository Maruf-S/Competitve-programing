class Solution:
 def catMouseGame(self, graph: List[List[int]]) -> int:
        DRAW, MOUSE, CAT = 0, 1, 2
        def gen_parent(mouse, cat, turn):
            if turn == MOUSE:
                for p in graph[cat]:
                    if p != 0:
                        yield mouse, p, CAT
            else:
                for p in graph[mouse]:
                    yield p, cat, MOUSE
        degree = dict()
        for i in range(len(graph)):
            for j in range(len(graph)):
                degree[i, j, MOUSE] = len(graph[i])
                degree[i, j, CAT] = len(graph[j]) - (0 in graph[j])
        color = defaultdict(int)
        queue = deque()
        for i in range(len(graph)):
            color[0, i, MOUSE] = MOUSE
            queue.append((0, i, MOUSE, MOUSE))
            color[0, i, CAT] = MOUSE
            queue.append((0, i, CAT, MOUSE))
            if i != 0:
                color[i, i, CAT] = CAT
                queue.append((i, i, CAT, CAT))
                color[i, i, MOUSE] = CAT
                queue.append((i, i, MOUSE, CAT))

        while queue:
            mouse, cat, turn, c = queue.popleft()
            for x, y, t in gen_parent(mouse, cat, turn):
                if color[x, y, t] == DRAW:
                    if t == c:
                        color[x, y, t] = c
                        if x == 1 and y == 2 and t == 1: return c
                        queue.append((x, y, t, c))
                    else:
                        degree[x, y, t] -= 1
                        if degree[x, y, t] == 0:
                            color[x, y, t] = 3 - t
                            if x == 1 and y == 2 and t == 1: return c
                            queue.append((x, y, t, 3 - t))
        return color[1, 2, 1]