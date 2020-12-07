def split(txt, seps):
    default_sep = seps[0]

    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.rstrip().split(default_sep)]
