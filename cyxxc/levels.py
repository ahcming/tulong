#! /usr/bin/env python3

# 游戏关卡, game levels

# 题目的原型
# terms是词条组合, #表示不存在, X表示待填
# words表示可选词列表
question1 = {
    "terms": [
        "飒", "#", "#", "#", "#", "#", "#", "#", "#",
        "X", "#", "#", "X", "#", "#", "#", "#", "#",
        "X", "X", "X", "出", "#", "#", "#", "#", "#",
        "X", "#", "#", "X", "#", "X", "X", "X", "弃",
        "#", "#", "X", "X", "X", "作", "#", "#", "#",
        "X", "#", "X", "#", "#", "X", "X", "智", "X",
        "胸", "X", "X", "X", "#", "X", "#", "X", "#",
        "X", "#", "败", "#", "#", "#", "#", "X", "#",
        "X", "#", "#", "#", "X", "X", "双", "X", "#"
    ],
    
    "words": [
        "自", "辈", "姿", "有", "自", "暴", "寿", "捶",
        "明", "英", "之", "成", "竹", "福", "全", "足",
        "聪", "别", "新", "得", "勇", "爽", "明", "顿",
        "双", "慧", "雄", "失", "意"
    ]
}

question = {
    "terms": [
        "#", "#", "#", "X", "怀", "X", "X", "#", "#",
        "#", "#", "#", "#", "X", "#", "#", "#", "#",
        "#", "X", "闲", "X", "X", "#", "X", "#", "#",
        "#", "X", "#", "#", "X", "X", "火", "X", "#",
        "#", "X", "#", "X", "#", "#", "X", "#", "#",
        "X", "得", "X", "X", "#", "X", "X", "X", "逃",
        "#", "#", "#", "人", "#", "#", "#", "#", "X",
        "X", "指", "X", "X", "#", "#", "#", "#", "X",
        "#", "#", "#", "#", "#", "#", "#", "#", "X"
    ],
    
    "words": [
        "之", "然", "鬼", "自", "在", "趁", "满", "难",
        "夭", "劫", "心", "间", "打", "悠", "心", "之",
        "自", "在", "胎", "意", "弹", "志", "恨", "急",
        "燎", "夭", "春"
    ]
}

# 候选词及数量, word -> count
words = {}

# 所有起始成语的位置及方向
# {"x": x, "y": y, "direct": True}
term_metas = []

def pretty():
    line = ""
    for idx, word in enumerate(question["terms"]):
        if word == "#":
            line += " "
        else:
            line += word
        line += "\t"

        if (idx + 1) % 9 == 0:
            print(line)
            line = ""
    print("--------------")
    for term in term_metas:
        print("-> %s" % term)

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

def bingo(x, y, direct, target):
    current = y * 9 + x
    for idx, word in enumerate(target):
        if direct:
            _index = current + idx
        else:
            _index = current + 9 * idx

        if question["terms"][_index] == "X":
            question["terms"][_index] = word
            words[word] -= 1

def init():
    _load_words()

    load_terms()

    
def _load_words():
    origin_words = question["words"]
    for word in origin_words:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

def get_term(term_meta):
    origin_terms = question["terms"]
    y = term_meta["y"]
    x = term_meta["x"]
    if term_meta["direct"]:
        return (origin_terms[y*9+x], origin_terms[y*9+x+1], origin_terms[y*9+x+2], origin_terms[y*9+x+3])
    else:
        return (origin_terms[y*9+x], origin_terms[(y+1)*9+x], origin_terms[(y+2)*9+x], origin_terms[(y+3)*9+x])

def load_terms():
    """
    加载所有成语, 只要第一个字
    """
    origin_terms = question["terms"]

    for idx, word in enumerate(origin_terms):
        if word == "#":
            continue

        y = idx // 9
        x = idx - 9 * y

        # 检查水平方向
        if x == 0:
            if origin_terms[idx+1] != "#":
                info = {"x": x, "y": y, "direct": True}
                term_metas.append(info)
            else:
                # print("---------1")
                pass

        elif x < 6:
            if origin_terms[idx+1] != "#" and origin_terms[idx-1] == "#":
                info = {"x": x, "y": y, "direct": True}
                term_metas.append(info)
            else:
                # print("---------2")
                pass

        else:
            # print("---------3")
            pass

        # 检查垂直方向
        if y == 0:
            if origin_terms[idx+9] != "#":
                info = {"x": x, "y": y, "direct": False}
                term_metas.append(info)
            else:
                # print("---------a")
                pass

        elif y < 6:
            if origin_terms[idx+9] != "#" and origin_terms[idx-9] == "#":
                info = {"x": x, "y": y, "direct": False}
                term_metas.append(info)
            else:
                # print("---------b")
                pass

        else:
            # print("---------c")
            pass


if __name__ == "__main__":
    init()

    print("=> %s" % words)

    for term in term_metas:
        print("=> %s" % (term, ))

    print("==> %s" % len(term_metas))