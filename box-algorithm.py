def do_intersect(point1_left, point1_right, point2_left, point2_right):
    return (min(point1_right, point2_right) > max(point1_left,point2_left))
def doBoxesOverlap(box1, box2):
    return (do_intersect(box1[0],box1[2],box2[0],box2[2]) and
            do_intersect(box1[1],box1[3], box2[1], box2[3]))