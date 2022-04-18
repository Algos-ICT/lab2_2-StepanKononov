import time
t_start = time.perf_counter()
f1 = open('input.txt')
n = int(f1.readline())
list_for_k = []
for line in f1:
    k, l, r = map(int, line.split(" "))
    list_for_k.append(k)

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Tree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Tree(value)
                else:
                    self.right.insert(value)
            else:
                self.value = value

    def pre_order(self, node):
        result_for_pre = []
        if node:
            result_for_pre.append(node.value)
            result_for_pre += self.pre_order(node.left)
            result_for_pre += self.pre_order(node.right)
        return result_for_pre

    def post_order(self, node):
        result_for_post = []
        if node:
            result_for_post = self.post_order(node.left)
            result_for_post += self.post_order(node.right)
            result_for_post.append(node.value)
        return result_for_post

    def in_order(self, node):
        result_for_in = []
        if node:
            result_for_in = self.in_order(node.left)
            result_for_in.append(node.value)
            result_for_in += self.in_order(node.right)
        return result_for_in
root = Tree(list_for_k[0])
for i in range(1, n):
    root.insert(list_for_k[i])
if not (n >= 1 and n <= 10**5):
    raise ValueError
centr_obh = root.in_order(root)
pr_obh = root.pre_order(root)
obr_obh = root.post_order(root)
f2 = open('output.txt', 'w')
for i in range(0, n-1):
    f2.write(str(centr_obh[i]) + " ")
f2.write(str(centr_obh[n - 1]) + "\n")
for i in range(0, n - 1):
    f2.write(str(pr_obh[i]) + " ")
f2.write(str(pr_obh[n - 1]) + "\n")
for i in obr_obh:
    f2.write(str(i) + " ")
f2.close()
print("Время работы алгоритма   ", (time.perf_counter() - t_start))
