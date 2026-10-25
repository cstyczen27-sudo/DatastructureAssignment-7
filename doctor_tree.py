class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.right = None
        self.left = None

class Doctor_tree:
    def __init__(self):
        self.root = None

    def insert(self, parent_node, employee_name, side, current_node=None):

        if self.root is None:
            print("Tree is empty. Cannot insert without root")
            return

        if current_node is None:
            current_node = self.root

        if current_node.name == parent_node:
            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(employee_name)
                return True
            elif side == "right" and current_node.right is None:
                current_node.right = DoctorNode(employee_name)
                return True
            else:
                return True

        found_left = False
        found_right = False

        if current_node.left:
            found_left = self.insert(parent_node, employee_name, side, current_node.left)

        if current_node.right and not found_left:
            found_right = self.insert(parent_node, employee_name, side, current_node.right)

        if not (found_left or found_right):
            if current_node == self.root:
                return f"Parent node {parent_node} not found in the tree"
            return False

        return True

    def preorder(self, node):
        if node is None:
            return []
        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result

    def inorder(self, node):
        if node is None:
            return[]
        result = []
        result += self.preorder(node.left)
        result.append(node.name)
        result += self.preorder(node.right)

        return result

    def postorder(self,node):
        if node is None:
            return []
        result = []
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        result.append(node.name)
        return result




tree = Doctor_tree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print(tree.preorder(tree.root))
print(tree.inorder(tree.root))
print(tree.postorder(tree.root))
# Test your DoctorTree and DoctorNode classes here
