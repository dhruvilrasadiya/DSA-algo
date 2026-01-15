def z_algorithm_search(text: str, pattern: str) -> list:

    if pattern == "":
        return list(range(len(text) + 1))
    if text == "" or len(pattern) > len(text):
        return []

    combined = pattern + "$" + text
    z = build_z_array(combined)

    matches = []
    pattern_length = len(pattern)

    for i in range(pattern_length + 1, len(combined)):
        if z[i] == pattern_length:
            matches.append(i - pattern_length - 1)

    return matches

def build_z_array(s: str) -> list:

    n = len(s)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z

text = "ABCCDDAECDDFGCDD"
pattern = "CDD"
result = z_algorithm_search(text, pattern)
print(result)