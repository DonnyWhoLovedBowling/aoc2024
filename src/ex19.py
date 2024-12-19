def fits(shawl):
    global  pattern_lens, patterns
    ret = 0
    if shawl in shawl_map:
        return shawl_map[shawl]
    for i in filter(lambda x: x <= len(shawl), pattern_lens):
        part = shawl[0:i]
        if part in patterns:
            if part == shawl:
                ret += 1
            ret += fits(shawl[i:])
    shawl_map[shawl] = ret
    return ret

if __name__ == '__main__':
    in_file = open("../data/ex19.txt")
    shawl_map = dict()
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    patterns = lines[0].split(', ')
    pattern_lens = {len(p) for p in patterns}
    shawls = lines[2:]

    ans_1 = 0
    ans_2 = 0
    for i, s in enumerate(shawls):
        ways = fits(s.strip())
        if ways > 0:
            ans_1 += 1
        ans_2 += ways

    print(ans_1)
    print(ans_2)