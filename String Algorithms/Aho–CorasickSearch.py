from collections import deque, defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []

def build_trie(patterns):
    root = TrieNode()

    for pattern in patterns:
        node = root
        for ch in pattern:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.output.append(pattern)

    return root

def build_failure_links(root):
    queue = deque()
    root.fail = root

    for child in root.children.values():
        child.fail = root
        queue.append(child)

    while queue:
        current = queue.popleft()

        for ch, child in current.children.items():
            fallback = current.fail
            while fallback != root and ch not in fallback.children:
                fallback = fallback.fail

            child.fail = fallback.children[ch] if ch in fallback.children else root
            child.output.extend(child.fail.output)
            queue.append(child)

def aho_corasick_search(text: str, patterns: list) -> dict:

    if not patterns:
        return {}
    if text == "":
        return {p: [] for p in patterns}

    root = build_trie(patterns)
    build_failure_links(root)

    result = defaultdict(list)
    node = root

    for i, ch in enumerate(text):
        while node != root and ch not in node.children:
            node = node.fail

        if ch in node.children:
            node = node.children[ch]
        else:
            node = root

        for pattern in node.output:
            result[pattern].append(i - len(pattern) + 1)

    for p in patterns:
        result.setdefault(p, [])

    return dict(result)


text = "ahishers"
pattern = ["he", "she", "hers", "his"]
result = aho_corasick_search(text, pattern)
print(result)