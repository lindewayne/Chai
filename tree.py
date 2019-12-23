class Tree():

    def __init__(self, name, nestedList, zi):
        self.name = name
        self.structure = nestedList[0]
        first = nestedList[1]
        second = nestedList[2]
        if len(nestedList) == 4:
            self.cross = nestedList[-1]
        if isinstance(first, str):
            if first in zi:
                self.first = Tree(first, zi[first], zi)
            else:
                self.first = first
        else:
            self.first = Tree('', first, zi)
        if isinstance(second, str):
            if second in zi:
                self.second = Tree(second, zi[second], zi)
            else:
                self.second = second
        else:
            self.second = Tree('', second, zi)

    def flatten(self):
        """
        输入：树
        输出：将所有嵌套列表展开，并删去结构操作符
        """
        stack = [self]
        componentList = []
        while stack:
            node = stack.pop()
            if isinstance(node, str):
                componentList.append(node)
            else:
                stack.extend([node.second, node.first])
        return componentList

    def veryFirst(self):
        """
        """
        node = self
        while isinstance(node, Tree):
            node = node.first
        return node