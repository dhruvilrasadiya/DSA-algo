def rabin_karp_search(text: str, pattern: str) -> list:

    if pattern == "":
        return list(range(len(text) + 1))
    if text == "" or len(pattern) > len(text):
        return []
    base = 256
    mod = 10**9 + 7

    n = len(text)
    m = len(pattern)

    pattern_hash = 0
    window_hash = 0
    h = 1

    for _ in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod

    matches = []

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                matches.append(i)

        if i < n - m:
            window_hash = (
                window_hash
                - ord(text[i]) * h
            ) % mod
            window_hash = (
                window_hash * base
                + ord(text[i + m])
            ) % mod
            window_hash = (window_hash + mod) % mod

    return matches


text = "ABCCDDAECDDFGCDD"
pattern = "CDD"
result = rabin_karp_search(text, pattern)
print(result)