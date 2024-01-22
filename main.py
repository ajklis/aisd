import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_collisions(circles):
    # Check the boundary condition
    if len(circles) < 2:
        return []

    # Sort circles based on x-coordinate
    circles.sort()

    intersecting_pairs = []
    closest_pair_in_strip(circles, 0, len(circles), intersecting_pairs)

    return intersecting_pairs

def closest_pair_in_strip(circles, start, end, intersecting_pairs):
    if end - start <= 3:
        # If the strip is small, use brute-force
        for i in range(start, end):
            for j in range(i + 1, end):
                if circles_intersect(circles[i], circles[j]):
                    intersecting_pairs.append((circles[i], circles[j]))

    else:
        middle = (start + end) // 2
        closest_pair_in_strip(circles, start, middle, intersecting_pairs)
        closest_pair_in_strip(circles, middle, end, intersecting_pairs)

        middle_strip = [p for p in circles if abs(p[0] - circles[middle][0]) < 2]
        for i in range(len(middle_strip)):
            for j in range(i + 1, len(middle_strip)):
                if middle_strip[j][1] - middle_strip[i][1] >= 2:
                    break
                if circles_intersect(middle_strip[i], middle_strip[j]):
                    intersecting_pairs.append((middle_strip[i], middle_strip[j]))

def circles_intersect(circle1, circle2):
    # Check if two circles intersect
    radius_sum = 1  # Assuming the radius of all circles is 1
    return distance(circle1, circle2) < 2 * radius_sum

# Example usage
circles = [(0, 0), (1, 1), (2, 1), (3, 3), (4, 4)]
result = find_collisions(circles)
print("Intersecting pairs of circles:", result)
