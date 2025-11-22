for _ in range(int(input())):
    n, m = map(int, input().split())


    # center angle of regular polygon at a center of circle = (2*pi)/n
    # now there are two polygons with number of sides n and m 
    # we want to fit, m-polygon inside n-polygon with same center.

    # n-polygon
    # this regular polygon will be inside a center
    # imagine two lines from center on to two consecutive vertices
    # the acute between these two lines = (2 * pi) / n

    # to fit m-polygon inside this 
    # we need to choose few vertices
    # say we choose 1, 2 vertices of n-polygon, the angle between them is as shown above
    # but the angle needed between two vertices of m-polygon is (2*pi)/m
    # if these align, that is n=m, then we can fit, (same polygon), but question says n!=m

    # what if we choose 1, 3 vertices of n-polygon, which gives 2 * (2 * pi) / m
    # if this matches with m-polygon's central angle, then we can pick these two vertices and make a side
    # like wise, we can pick all the m sides and fit the polygon

    # so, 2pi/m = k * (2pi/n) (some multiple)
    #       1/m = k* 1/n
    #       n = k * m
    # that m divides n

    print("YES" if n % m == 0 else "NO")