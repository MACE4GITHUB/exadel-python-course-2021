tree = {
    "node1": {
        "node11": {
            "node111": [1, 2, 3],
            "node112": [4, 5]
        },
        "node12": [6]
    },
    "node2": [7, 8, 9]
}


def collect_leaves(tree):
    if isinstance(tree, dict):
        leaves = []
        for sub_tree in tree.values():
            leaves.extend(collect_leaves(sub_tree))
        return leaves
    return tree


assert collect_leaves(tree) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# edge case: flat tree
assert collect_leaves([1, 2, 3]) == [1, 2, 3]
