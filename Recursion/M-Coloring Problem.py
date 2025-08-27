# https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1

# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        # empty adj graph list
        adj= [[] for i in range(v)]
        # putting adj vertices of that index
        for edge in edges:
            adj[edge[0]].append(edge[1]) 
            adj[edge[1]].append(edge[0])

        colors= [0] * v # set every node to 0 (not colored)

        return self.helper(0, adj, m, v, colors)

    def helper(self, node, adj, m, v, colors):
        # base case
        if node == v:
            return True
        # looping through every possible color
        for col in range(1, m+1):
            if self.isSafe(col, node, colors, adj):
                colors[node]= col # colored 'node' with "col" color
                if self.helper(node+1, adj, m, v, colors):
                    return True
                colors[node]= 0 # reset color

        return False

    def isSafe(self, col, node, colors, adj):
        for i in adj[node]:
            if colors[i] == col:
                return False
        return True
