#! python

class Tree:
    def __init__(self): # чтобы создавать узлы, нужно сначала создать дерево
        self.root = None

    def append(self, value):
        Node(value, self)

    def view(self): # для распределения значений по уровням нужно как-то считать количество вызовов рекурсивных
        self.root.view()

    def found(self, value):
        return self.root.found(value)

    def min_el(self):
        return self.root.min_el()

    def remove_root(self, value):
        if self.found(value).parent is None:
            to_del = self.found(value)
            if not to_del.smaller and not to_del.bigger:
                Node.__del__(to_del)
                self.root = None
                print('tree is over')
            if not to_del.smaller and to_del.bigger:
                self.root = to_del.bigger
                to_del.bigger.parent = None
                Node.__del__(to_del)
            if to_del.smaller and not to_del.bigger:
                self.root = to_del.smaller
                to_del.smaller.parent = None
                Node.__del__(to_del)
            if to_del.smaller and to_del.bigger:
                new_node = to_del.bigger.min_el()
                self.root = new_node
                new_val, tree = new_node.value, new_node.tree
                self.remove(new_node.value)  # удаляем ссылку на минимальный
                new_node.value, new_node.tree = new_val, tree
                new_node.smaller, new_node.bigger = to_del.smaller, to_del.bigger  # переписываем ссылки удаляемого
                to_del.smaller.parent = new_node
                if to_del.bigger:
                    to_del.bigger.parent = new_node # может не существовать!!!
                Node.__del__(to_del)

    def remove(self, value):
        if self.found(value):
            to_del = self.found(value)
            if to_del == self.root:
                self.remove_root(value)
            else:
                if not to_del.smaller and not to_del.bigger: # лист
                    if to_del.value > to_del.parent.value:
                        to_del.parent.bigger = None
                        Node.__del__(to_del)
                    else:
                        to_del.parent.smaller = None
                        Node.__del__(to_del)
                if not to_del.smaller and to_del.bigger: # один потомок
                    if to_del.value > to_del.parent.value: # у корня не существует родителя
                        to_del.bigger.parent = to_del.parent # скопировали родителя для ребёнка
                        to_del.parent.bigger = to_del.bigger # скопировали ребенка для родителя
                        Node.__del__(to_del)
                    else:
                        to_del.bigger.parent = to_del.parent
                        to_del.parent.smaller = to_del.bigger
                        Node.__del__(to_del)
                if to_del.smaller and not to_del.bigger: # у удаляемого есть только меньший
                    if to_del.value > to_del.parent.value:
                        to_del.smaller.parent = to_del.parent
                        to_del.parent.bigger = to_del.smaller
                        Node.__del__(to_del)
                    else:
                        to_del.smaller.parent = to_del.parent
                        to_del.parent.smaller = to_del.smaller
                        Node.__del__(to_del)
                if to_del.smaller and to_del.bigger: # два потомка
                    new_node = to_del.bigger.min_el()
                    new_val, tree = new_node.value, new_node.tree
                    self.remove(new_node.value) # удаляем ссылку на минимальный
                    new_node.value, new_node.tree = new_val, tree
                    new_node.parent, new_node.smaller, new_node.bigger = to_del.parent, to_del.smaller, to_del.bigger # переписываем ссылки удаляемого
                    to_del.smaller.parent = new_node
                    if to_del.bigger:
                        to_del.bigger.parent = new_node # может не существовать!!!
                    if to_del.value > to_del.parent.value: # и переписываем ссылки на новый в родителях
                        to_del.parent.bigger = new_node
                    else:
                        to_del.parent.smaller = new_node
                    Node.__del__(to_del)

    def get_arr(self):
        arr = []
        while self.root:
            node = self.min_el()
            arr.append(node.value)
            self.remove(node.value)
        return arr


class Node:
    def __init__(self, value, tree: Tree):
        self.smaller, self.bigger, self.parent = None, None, None
        self.tree, self.value = tree, value
        if self.tree.root:
            self.insert(self.tree.root)
        else:
            self.tree.root = self

    def insert(self, node): # вызываем сначала для корня дерева -- self.tree.root, этот аргумент прописать в ините
        if self.value > node.value:
            if not node.bigger:
                node.bigger = self
                self.parent = node
            else:
                self.insert(node.bigger)
        if self.value < node.value:
            if not node.smaller:
                node.smaller = self
                self.parent = node
            else:
                self.insert(node.smaller)
        if self.value == node.value:
            print('This value is already exist')

    def view(self):
        if self.parent:
            print(self.value, '(', self.parent.value, ')')
        else:
            print('ROOT', self.value)
        if self.bigger:
            Node.view(self.bigger)
        else:
            print('right end')
        if self.smaller:
            Node.view(self.smaller)
        else:
            print('left end')

    def found(self, value):
        if value == self.value:
            print('value exists')
            return self
        if value > self.value:
            if not self.bigger:
                print('No such value')
            else:
                return self.bigger.found(value)
        if value < self.value:
            if not self.smaller:
                print('No such value')
            else:
                return self.smaller.found(value)

    def __del__(self):
        self.smaller, self.bigger, self.parent, self.value, self.tree = None, None, None, None, None

    def min_el(self):
        current_node = self
        while current_node.smaller:
            current_node = current_node.smaller
        print(current_node.value)
        return current_node


if __name__ == "__main__":
    t1 = Tree()
    n1 = Node(3, t1)
    n2 = Node(7, t1)
    n3 = Node(1, t1)
    n4 = Node(2, t1)
    n5 = Node(0, t1)
    n6 = Node(5, t1)
    n7 = Node(9, t1)
    n8 = Node(4, t1)
    n9 = Node(6, t1)
    n10 = Node(8, t1)
    n11 = Node(10, t1)
    n1.view()

