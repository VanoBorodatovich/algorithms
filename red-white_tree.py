#! python


class RWTree:
    def __init__(self):
        self.root = None
        self.nill = Nill(self)

    def append(self, value):
        RWNode(value, self)

    def view(self):
        self.root.view()

    def found(self, value):
        return self.root.found(value)

    def min_el(self):
        return self.root.min_el()

    def black_height(self, node):
        count = 1
        current_node = node
        while current_node != 'is_over':
            if current_node.colour == 'black':
                count += 1
            print(current_node.value, ' ', current_node.colour)
            if current_node.colour == 'red':
                print(current_node.value, ' ', current_node.colour)
            if not current_node.parent:
                current_node = 'is_over'
                print('ROOT ', count)
                return count
            else:
                current_node = current_node.parent

    def make_true(self):
        height_max = 0
        long_branch = []
        for f in self.nill.arr:
            if self.black_height(f) > height_max:
                height_max = self.black_height(f)
        for f in self.nill.arr: # чтобы не гонять второй раз цикл, в первом можно создать словарь, с ключами - листьями
            # и значениями - длинной
            if self.black_height(f) == height_max:
                f.colour = 'red'


class RWNode:
    def __init__(self, value, tree: RWTree):
        self.smaller, self.bigger, self.parent = tree.nill, tree.nill, None
        tree.nill.arr.append(self)
        self.tree, self.value = tree, value
        if self.tree.root:
            self.rebuild(self.tree.root)
            self.colour = 'black'  # при перестройке из простого бин, все узлы добавляемые - чёрные,а вставку я не прописал
        else:
            self.tree.root = self
            self.colour = 'black'

    def rebuild(self, node): # вызываем сначала для корня дерева -- self.tree.root, этот аргумент прописать в ините
        if self.value > node.value:
            if node.bigger == self.tree.nill:
                node.bigger = self
                if node.smaller != self.tree.nill:
                    self.tree.nill.arr.remove(node)
                self.parent = node
            else:
                self.rebuild(node.bigger)
        if self.value < node.value:
            if node.smaller == self.tree.nill:
                node.smaller = self
                if node.bigger != self.tree.nill:
                    self.tree.nill.arr.remove(node)
                self.parent = node
            else:
                self.rebuild(node.smaller)
        if self.value == node.value:
            print('This value is already exist')

    def view(self):
        if self.parent:
            print(self.value, '(', self.parent.value, ')', self.colour)
        else:
            print('ROOT', self.value)
        if self.bigger != self.tree.nill:
            self.bigger.view()
        else:
            print('right end')
        if self.smaller != self.tree.nill:
            self.smaller.view()
        else:
            print('left end')

    def found(self, value):
        if value == self.value:
            print('value exists')
            return self
        if value > self.value:
            if self.bigger == self.tree.nill:
                print('No such value')
            else:
                return self.bigger.found(value)
        if value < self.value:
            if self.smaller == self.tree.nill:
                print('No such value')
            else:
                return self.smaller.found(value)

    def __del__(self):
        if self.bigger == self.tree.nill or self.smaller == self.tree.nill:
            self.tree.nill.arr.remove(self)
        self.smaller, self.bigger, self.parent, self.value, self.tree, self.colour = None, None, None, None, None, None

    def min_el(self):
        current_node = self
        while current_node.smaller != self.tree.nill:
            current_node = current_node.smaller
        print(current_node.value)
        return current_node


class Nill:
    def __init__(self, tree: RWTree):
        self.tree = tree
        self.arr = []


def get_balanced_tree(arr, new_tree: RWTree):
    if len(arr) <= 2:
        for f in range(len(arr)):
            new_tree.append(arr[f])
        return new_tree
    else:
        if len(arr) % 2:
            h = len(arr) // 2
            arr1 = arr[0:h]
            arr2 = arr[h + 1: len(arr)]
            new_tree.append(arr[h]) # добавляем средний элемент
            get_balanced_tree(arr1, new_tree)
            get_balanced_tree(arr2, new_tree)
        else:
            h = len(arr) // 2
            new_tree.append(arr[h]) # добавляем первый из правой половины
            arr1 = arr[0:h]
            arr2 = arr[h + 1: len(arr)]
            get_balanced_tree(arr1, new_tree)
            get_balanced_tree(arr2, new_tree)


# t2 = RWTree()
# RWNode(3, t2)
# RWNode(6, t2)
# nt = RWTree()
# arr = [1,2,3,4,5,6,7,8,9,10]
# get_balanced_tree(arr, nt)
# nt.make_true()

from project1.py.day_18_11.binary_tree import Tree, Node


# чтобы получить красно-черное дерево, нужно сначала создать его пустое и передать функции
def bin_to_rw(bin_t: Tree, rw_t: RWTree):
    arrr = bin_t.get_arr()
    get_balanced_tree(arrr, rw_t)
    rw_t.make_true()
