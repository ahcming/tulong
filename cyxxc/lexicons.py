#! /usr/bin/env python3

# 词库相关的操作

db_path = "/Users/ahcming/workspace/github/tulong/cyxxc/word.db"

indexs = {}

def init():
    _load()


def _load():
    db = open(db_path, "r")
    count = 0

    for term in db.readlines():
        _build_index(term.strip())
        count = count + 1

    # print("--> %s" % indexs)
    db.close()


def _build_index(term):
    # print(term)
    for (idx, word) in enumerate(term):
        word_key = "%s_%d" % (word, idx)
        if word_key in indexs:
            indexs.get(word_key).append(term)
        else:
            indexs[word_key] = [term]


def candidates(targets, words):
    """
    查询候选词
    """
    times = len(targets)

    mays = {}
    for (word, index) in targets.items():
        word_key = "%s_%d" % (word, index)
        right_terms = indexs.get(word_key)
        # print("[debug] target: %s, word key: %s" % (word, word_key) )

        for term in right_terms:
            if term in mays:
                mays[term] += 1
            else:
                mays[term] = 1
        
    after = []
    for term, count in mays.items():
        if count == times:
            all_in = True
            for idx, wd in enumerate(term):
                if wd in targets and targets[wd] == idx:
                    continue

                if wd not in words or words[wd] <= 0:
                    # print("==> %s, %s, %s, %s, %s, idx1: %s, %s, idx2: %s" % (targets, term, wd, idx, wd in targets, targets.get(wd), wd not in words, words.get(wd)))
                    all_in = False
                    break
            
            if all_in:
                after.append(term)
            else:
                # print("[%s] not all in words, term: %s, word: %s, index: %s, is in title: %s, is in words: %s, times: %s, words: %s" % (targets, term, wd, idx, (wd in targets and targets[wd] == idx), (wd in words), words.get(wd), words))
                pass

    # print("word: %s, times: %s, result: %s" % (targets, times, after))
    return after


if __name__ == "__main__":
    init()

    choices = {'自': 0, '辈': 0, '姿': 0, '有': 0, '暴': 0, '寿': 0, '捶': 0, '明': 0, '英': 0, '之': 0, '成': 0, '竹': 0, '福': 0, '全': 0, '足': 0, '聪': 0, '别': 1, '新': 1, '得': 0, '勇': 0, '爽': 0, '顿': 0, '双': 0, '慧': 0, '雄': 0, '失': 0, '意': 0}
    print(candidates({"出": 1, "意": 3}, choices))