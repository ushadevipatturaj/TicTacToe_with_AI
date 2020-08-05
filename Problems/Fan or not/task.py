def add_viewer(name, fans=None):
    if fans is None:
        not_fans = []
        not_fans.append(name)
        return not_fans
    else:
        fans.append(name)
        return fans