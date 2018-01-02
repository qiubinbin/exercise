def map_cn(m):
    if isinstance(m, str):
        return m.title()
    else:
        return m


print(list(map(map_cn, ['qiu', 77, 'bin'])))
