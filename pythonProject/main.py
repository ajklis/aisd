import math
import PySimpleGUI as sg

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_collisions(circles):
    if len(circles) < 2:
        return []

    circles.sort()

    intersecting_pairs = []
    closest_pair_in_strip(circles, 0, len(circles), intersecting_pairs)

    return intersecting_pairs

def closest_pair_in_strip(circles, start, end, intersecting_pairs):
    if end - start <= 3:
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
    radius_sum = 1
    return distance(circle1, circle2) < 2 * radius_sum

def main():
    layout = [
        [sg.Text("Wprowadź współrzędne punktów (x, y):")],
        [sg.Multiline(size=(40, 6), key="COORDINATES")],
        [sg.Button("Znajdź przecinające się pary"), sg.Button("Zamknij")],
        [sg.Text("Wyniki:", size=(40, 1))],
        [sg.Output(size=(40, 6))]
    ]

    window = sg.Window("Znajdowanie przecinających się kółek", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Zamknij":
            break
        elif event == "Znajdź przecinające się pary":
            coordinates_str = values["COORDINATES"]
            points = [tuple(map(float, w.split(","))) for w in coordinates_str.split("\n") if w]

            if points:
                results = find_collisions(points)
                print("Przecinające się pary kółek:")
                for pair in results:
                    print(pair)
                print("\n---\n")

    window.close()

if __name__ == "__main__":
    main()
