class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.left = None
        self.right = None

class Student:
    def __init__(self, name, address ,mark):
        self.name = name
        self.address = address
        self.mark = mark

class StudentManagement:
    def __init__(self):
        self.root = None
    
    def student_insert(self, root, id, data):
        if self.root is None:
            self.root = Node(id, data)
        elif root is None:
            root = Node(id, data)
        else:
            if root.id > id:
                root.left = self.student_insert(root.left, id, data)
            elif root.id < id:
                root.right = self.student_insert(root.right, id, data)
            else:
                print("ID not avaiable")
            return root
        
    def student_search(self, root, id):
        if self.root is None:
            print("none to search")
        elif root is None:
            return
        else:
            if root.id == id:
                print(f"Student id: {root.id}\n"
                        f"Student name: {root.data.name}\n"
                        f"Student address: {root.data.address}\n"
                        f"Student mark: {root.data.mark}")
            elif root.id > id:
                root.left = self.student_search(root.left, id)
            elif root.id < id:
                root.right = self.student_search(root.right, id)
            return root

    def student_update(self, root, id, name = None, address = None, mark = None):
        if self.root is None:
            print("None is here to update")
        elif root is None:
            return
        else:
            if root.id > id:
                root.left = self.student_update(root.left, id ,name, address, mark)
            elif root.id < id:
                root.right = self.student_update(root.right, id, name, address, mark)
            elif root.id == id:
                if name:
                    root.data.name = name
                if address:
                    root.data.address = address
                if mark:
                    root.data.mark = mark
            return root

    def student_delete(self,root, id):
        if self.root is None:
            print("None for delete")
        elif root is None:
            return
        else:
            if root.id > id:
                root.left = self.student_delete(root.left, id)
            elif root.id < id:
                root.right = self.student_delete(root.right, id)
            elif root.id == id:
                if not root.left and not root.right:
                    return None
                elif not root.left and root.right:
                    return root.right
                elif root.left and not root.right:
                    return root.left
                else:
                    next_student = root.right
                    if next_student.left: next_student = next_student.left
                    root.id = next_student
                    root.data = next_student.data
                    root.right = self.student_delete(root.right, next_student.id)
                    
                return root
            return root
    
    def show_infor(self, root, type):
        if self.root is None:
            print("None to show")
        elif root is None:
            return
        else:
            if type == 'preorder':
                print(f"Student id: {root.id}\n"
                        f"Student name: {root.data.name}\n"
                        f"Student address: {root.data.address}\n"
                        f"Student mark: {root.data.mark}")
                self.show_infor(root.left, type)
                self.show_infor(root.right, type)
            elif type == 'inorder':
                self.show_infor(root.left, type)
                print(f"Student id: {root.id}\n"
                        f"Student name: {root.data.name}\n"
                        f"Student address: {root.data.address}\n"
                        f"Student mark: {root.data.mark}")
                self.show_infor(root.right, type)
            
            elif type == 'postorder':
                self.show_infor(root.left, type)
                self.show_infor(root.right, type)
                print(f"Student id: {root.id}\n"
                        f"Student name: {root.data.name}\n"
                        f"Student address: {root.data.address}\n"
                        f"Student mark: {root.data.mark}")
            return root

def Menu():
    print("#"*10)
    print("1. Insert Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show all Students")
    print("6. Quit")
    print("#"*10)
    
def Main():
    tree = StudentManagement()
    while True:
        Menu()
        action = input("Enter your action: ")
        if action == '1':
            try:
                student_id = int(input("Enter studetn id: "))
                student_name = input("Enter student name: ")
                student_address = input("Enter student address: ")
                student_mark = float(input("Enter student mark: "))
            except:
                print("Wrong ID or Mark")
            else:
                student = Student(student_name, student_address, student_mark)
                tree.student_insert(tree.root, student_id, student)

        elif action == '2':
            try:
                search_id = int(input("Enter search ID: "))
            except: 
                print("Wrong ID")
            else:
                tree.student_search(tree.root, search_id)

        elif action == '3':
            try:
                update_id = int(input("Enter update id: "))
            except:
                print("wrong ID")
            else:
                try:
                    update_name = input("Enter name: ")
                    update_address = input("Enter address: ")
                    update_mark = float(input("Enter mark: "))
                except:
                    update_mark = None
                else:
                    tree.root = tree.student_update(tree.root, 
                                                    update_id, 
                                                    update_name, 
                                                    update_address, 
                                                    update_mark)
        elif action == '4':
            try:
                delete_id = int(input("Enter id: "))
            except:
                print("not that ID")
            else:
                tree.root = tree.student_delete(tree.root, delete_id)
        elif action == '5':
            all_type = ['preorder', 'inorder', 'postorder']
            enter_type = input("Enter type: 'preorder', 'inorder', 'postorder' : ")
            if enter_type not in all_type:
                print("Wrong type")
            else: 
                tree.root = tree.show_infor(tree.root, enter_type)
        elif action == '6':
            print("Bye!")
            break

if __name__ == "__main__":
    Main()      
