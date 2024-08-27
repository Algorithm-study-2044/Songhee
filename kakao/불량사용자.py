from itertools import product

def is_banned(uid, bid):

    n_uid = len(uid)
    n_bid = len(bid)

    # length
    if n_uid != n_bid:
        return False

    # matching
    for i in range(n_uid):
        if bid[i] == '*':
            continue
        elif bid[i] != uid[i]:
            return False

    return True

def solution(user_id, banned_id):

    banned = []

    n_uid = len(user_id)
    n_bid = len(banned_id)

    for i in range(n_bid):
        tmp = []
        for j in range(n_uid):
            if is_banned(user_id[j], banned_id[i]):
                tmp.append(j)
        banned.append(tmp)

    # tmp = [[0,1,2],[3]]
    # comb = [(0,3), (1,3), (2,3)]
    comb = list(product(*banned))

    # to eliminate duplicate answer
    ans_set = set()
    for elem in comb:
        set_elem = set(list(elem))
        # to ban everything
        if len(set_elem) == len(banned):
            elem = list(elem)
            elem.sort()
            elem = tuple(elem)
            # to prevent duplication
            ans_set.add(elem)

    answer = len(ans_set)

    return answer