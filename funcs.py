def nestedforloop(bool):
    year = ['2015', '2016', '2017', '2018']
    words = ['hi', 'bye', 'sigh', 'fly', 'why']
    order = ['first', 'last']

    sumlist = []
    for y in year:
        if bool == 'True':
            new = '{}:{}'.format(y,y)
        else:
            new = y
        for w in words:
            for o in order:
                args = ':'.join([new, w, o])

                sumlist.append(args)

    return(sumlist)
