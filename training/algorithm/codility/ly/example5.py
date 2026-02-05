from typing import List, Dict, Set
from collections import defaultdict


def solution(size: int, edges: List[int]) -> bool:
    """Detect cycle in directed graph"""
    graph: Dict[int, List[int]] = defaultdict(list)
    
    for i in range(size):
        graph[i] = []
    
    for i in range(0, len(edges), 2):
        from_node = edges[i]
        to_node = edges[i + 1]
        graph[from_node].append(to_node)
    
    visited: Set[int] = set()
    in_stack: Set[int] = set()
    
    for node in graph.keys():
        if is_directed_graph(node, graph, visited, in_stack):
            return True
    
    return False


def is_directed_graph(
    node: int, 
    graph: Dict[int, List[int]], 
    visited: Set[int], 
    in_stack: Set[int]
) -> bool:
    """DFS to detect cycle"""
    if node in in_stack:
        return True
    if node in visited:
        return False
    
    visited.add(node)
    in_stack.add(node)
    
    for neighbor in graph.get(node, []):
        if is_directed_graph(neighbor, graph, visited, in_stack):
            return True
    
    in_stack.remove(node)
    return False


def main():
    size = 3
    edges = [0, 1, 1, 2, 2, 0]
    print(solution(size, edges))  # True (has cycle)


if __name__ == "__main__":
    main()
