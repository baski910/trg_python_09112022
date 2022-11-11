def add(x,y):
    x += str(y)
    return x

def add_2(x,y):
    if y % 20000 == 0:
        z = []
        for q in range(400000):
            z.append(q)

def main():
    a = []
    for n in range(200000):
        add(a,n)
        add_2(a,n)

if __name__ == '__main__':
    #import cProfile
    #cProfile.run('main()')
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()


