#!/usr/bin/env python

"""
An iterative implementation of depth-first search from:
"Python Algorithms: Mastering Basic Algorithms in the Python Language"
by  	Magnus Lie Hetland
ISBN: 	9781484200551 
Input consists of a simple graph of { node: [list of neighbors] } plus a source and target node.
"""

def dfs (graph, src, tgt):
    """Return a path from the source (src) to the target (tgt) in the graph using depth-first search"""
    
    if not graph.has_key(src):
        raise AttributeError("The source '%s' is not in the graph" % src)
    if not graph.has_key(tgt):
        raise AttributeError("The target '%s' is not in the graph" % tgt)

    path = []
    
    queue = []
    queue.append(src)
    while queue:
        node = queue.pop()
        if node not in path:
            path.append(node)
            if node == tgt:
                break
            queue.extend(graph[node])
            
    return path


"""
Test using the graph from: 
https://commons.wikimedia.org/wiki/File:Graph_with_Chordless_and_Chorded_Cycles.svg
"""

test = {
    "a": ["b", "f"],
    "b": ["a", "c", "g"],
    "c": ["b", "d", "g", "l"],
    "d": ["c", "e", "k"],
    "e": ["d", "f"],
    "f": ["a", "e"],
    "g": ["b", "c", "h", "l"],
    "h": ["g", "i"],
    "i": ["h", "j", "k"],
    "j": ["i", "k"],
    "k": ["d", "i", "j", "l"],
    "l": ["c", "g", "k"],
}

# unlike BFS, this will *not* always find the shortest paths
assert dfs(test, "a", "e") == ['a', 'f', 'e']
assert dfs(test, "a", "i") != ['a', 'b', 'g', 'h', 'i']      # finds: ['a', 'f', 'e', 'd', 'k', 'l', 'g', 'h', 'i']
assert dfs(test, "a", "l") != ['a', 'b', 'c', 'l']           # finds: ['a', 'f', 'e', 'd', 'k', 'l']
assert len(dfs(test, "b", "k")) == len(['b', 'c', 'd', 'k']) # finds: ['b', 'g', 'l', 'k'] which is ok b/c of length