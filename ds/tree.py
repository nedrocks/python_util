class Tree(list):
    """Tree implementation with each node represented by a list of child nodes.
    """
    def __init__(self, attr):
        self.attr = attr
        list.__init__(self, [])

    def __repr__(self):
        return str(Tree.list_repr(self))

    @classmethod
    def list_repr(cls, root, depth=0, repr_list=None):
        if not repr_list:
            repr_list = list()
        if len(repr_list) < depth + 1:
            repr_list.append(list())
        repr_list[depth].append(root.attr)
        for node in root:
            cls.list_repr(node, depth + 1, repr_list)
        return repr_list