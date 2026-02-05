from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Point:
    point: Tuple[int, int]
    dist: int


def distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    """Calculate squared distance between two points"""
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    return dx * dx + dy * dy


def k_closest_points(points: List[Tuple[int, int]], p: Tuple[int, int], k: int) -> List[Tuple[int, int]]:
    """
    Find K closest points to point P based on distance.
    
    Args:
        points: List of points [(x0,y0)......(xn,yn)]
        p: Reference point (px,py)
        k: Number of closest points to return
    
    Returns:
        List of k closest points
    """
    if not points or not p or len(p) != 2 or k <= 0:
        return []
    
    if k >= len(points):
        k = len(points)
    
    # Create list of Point objects with distances
    point_list = []
    for point in points:
        dist = distance(point, p)
        point_list.append(Point(point, dist))
    
    # Sort by distance
    point_list.sort(key=lambda x: x.dist)
    
    # Return k closest points
    return [point_list[i].point for i in range(k)]


def main():
    points = [
        (1, 2),
        (3, 4),
        (1, 1),
        (5, 5)
    ]
    
    p = (0, 0)
    k = 2
    
    closest_points = k_closest_points(points, p, k)
    
    print(f"The {k} closest points to p are:")
    for point in closest_points:
        print(f"({point[0]}, {point[1]})")
    
    # Refactored version using sorted
    print(f"\nRefactored: The {k} closest points to p are:")
    sorted_points = sorted(points, key=lambda point: distance(point, p))[:k]
    for point in sorted_points:
        print(f"({point[0]}, {point[1]})")


if __name__ == "__main__":
    main()
