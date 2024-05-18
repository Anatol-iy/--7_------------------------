class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def sum_of_values(root):
    if root is None:
        return 0
    return root.val + sum_of_values(root.left) + sum_of_values(root.right)

# Створюємо дерево і вставляємо в нього деякі значення
root = None
values = [10, 5, 15, 3, 7, 12, 20]
for value in values:
    root = insert(root, value)

# Знаходження суми всіх значень у дереві
sum_values = sum_of_values(root)
print("Сума всіх значень у дереві:", sum_values)
