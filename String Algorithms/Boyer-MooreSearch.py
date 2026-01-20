def build_bad_char_table(pattern: str) -> dict:

    bad_char = {}
    for i, ch in enumerate(pattern):
        bad_char[ch] = i
    return bad_char


def build_good_suffix_table(pattern: str) -> list:

    m = len(pattern)
    shift = [0] * (m + 1)
    border = [0] * (m + 1)

    i = m
    j = m + 1
    border[i] = j

    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1 if j - 1 < m else 0]:
            if shift[j] == 0:
                shift[j] = j - i
            j = border[j]
        i -= 1
        j -= 1
        border[i] = j

    j = border[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = border[j]

    return shift


def boyer_moore_search(text: str, pattern: str) -> list:

    if pattern == "":
        return list(range(len(text) + 1))
    if text == "" or len(pattern) > len(text):
        return []

    n = len(text)
    m = len(pattern)

    bad_char = build_bad_char_table(pattern)
    good_suffix = build_good_suffix_table(pattern)

    matches = []
    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            matches.append(s)
            s += good_suffix[0]
        else:
            bad_char_shift = j - bad_char.get(text[s + j], -1)
            good_suffix_shift = good_suffix[j + 1]
            s += max(bad_char_shift, good_suffix_shift)

    return matches


text = "ABCCDDAECDDFGCDD"
pattern = "CDD"
result = boyer_moore_search(text, pattern)
print(result)