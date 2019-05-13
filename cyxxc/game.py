#! /usr/bin/env python3.6

import levels
import lexicons


lexicons.init()
levels.init()

def intersection(_words):
    ls = []
    times = 0

    # print("@@@@@@: A: %s, B: %s: C: %s, D: %s" % (_words[0], _words[1], _words[2], _words[3]))
    _targets = {}

    if _words[0] != "X":
        _targets[_words[0]] = 0

    if _words[1] != "X":
        _targets[_words[1]] = 1

    if _words[2] != "X":
        _targets[_words[2]] = 2

    if _words[3] != "X":
        _targets[_words[3]] = 3

    inters = lexicons.candidates(_targets, levels.words)
    # print("(%s) intersection end, result: %s" % (_words, inters))
    return inters

def find(term_meta, words):
    # print("--> %s" % term_meta)
    x = term_meta["x"]
    y = term_meta["y"]
    direct = term_meta["direct"]

    # 求交集
    _inters = intersection(words)
    size = len(_inters)
    
    if size == 1:
        # bingo
        levels.bingo(x, y, direct, _inters[0])
        print("current local find candidates: (%s, %s) -> %s # choices: %s" % (term_meta, words, _inters, list(filter(lambda item: item[1] > 0, levels.words.items()))))
        return True

    elif size == 0:
        # error
        # print("level error, no candidates: (%s, %s) -> %s" % (x, y, _words))
        raise Exception("level error, no candidates: (%s, %s) -> %s" % (x, y, words))
        return False

    else:
        # next
        print("current local has too many candidates: (%s, %s) -> %s # choices: %s" % (term_meta, words, _inters, list(filter(lambda item: item[1] > 0, levels.words.items()))))
        return False

def play():
    _isEnd = False
    run_times = 0
    while _isEnd is False:
        _find = False
        for _term_meta in levels.term_metas:
            _term = levels.get_term(_term_meta)
            if "X" not in _term:
                continue

            if find(_term_meta, _term):
                _find = True
                # break

        if _find:
            # levels.load_terms()
            _isEnd = False
        else:
            _isEnd = True

        run_times += 1
        print("loop times [%s] complete!" % run_times)
        print()

levels.pretty()

play()
levels.pretty()
