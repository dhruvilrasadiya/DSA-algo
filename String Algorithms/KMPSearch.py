def kmp_search(text: str, pattern: str) -> list:
    if pattern == "":
        return list(range(len(text) + 1))
    if text == "" or len(pattern) > len(text):
        return []

    lps = build_lps(pattern)
    matches = []

    i = 0
    j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches


def build_lps(pattern: str) -> list:
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


text = "ABABDABACDABABCABAB"
pattern = "BACDA"
result = kmp_search(text, pattern)
print(result)