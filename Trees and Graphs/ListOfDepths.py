# # Implement Linked List Data Structure
# from collections import defaultdict
#
#
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# class GraphNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class Graph:
#     def __init__(self, vertices):
#         self.vertices = vertices
#         self.graph = defaultdict(list)
#
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     def breadFirstSearch(self, root):
#         visited = [False] * self.vertices
#         queue = []
#         if root is None:
#             return None
#
#         queue.append(root)
#         visited[root] = True
#         ListsOfLists = []
#         while queue:
#             innerList = []
#             node = queue.pop()
#             if node.left :
#                 innerList.append(node.left)
#             if node.right:
#                 innerList.append(node.right)
# 
#             for i in self.graph[node]:
#                 if visited[i] == False:
#                     queue.append(i)
#                     visited[i] = True
#
