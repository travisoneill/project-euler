from benchmark import benchmark

triangular = lambda n: (n * n + n) // 2
def num_rectangles_contained(x, y):
    return triangular(x) * triangular(y)

def calculate_search_area(target):
    long_side = 1
    rectangles = 0
    while rectangles < target:
        rectangles = num_rectangles_contained(1, long_side)
        long_side += 1
    perim_upper_limit = long_side + 1
    current_best_diff = abs(target - rectangles)
    rectangles = 0
    side = 0
    while rectangles < target - current_best_diff:
        rectangles = num_rectangles_contained(side, side)
        side += 1
    return {'upper_bound': perim_upper_limit, 'lower_bound': side * 2}


@benchmark()
def search(target):
    search_area = calculate_search_area(target)
    min_diff = target
    optimum = None
    for perimeter in range(search_area['lower_bound'], search_area['upper_bound']):
        for x in range(1, perimeter // 2):
            y = perimeter - x
            rects = num_rectangles_contained(x, y)
            diff = abs(target - rects)
            if diff < min_diff:
                optimum = (x, y)
                min_diff = diff
            if rects > target:
                break
    print(optimum)
    print(rc(*optimum))
    return optimum[0] * optimum[1]

# CLI shortcuts
rc = num_rectangles_contained
cs = calculate_search_area
