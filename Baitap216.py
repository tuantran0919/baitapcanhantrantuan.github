import tkinter as tk
from tkinter import messagebox

# Node của danh sách liên kết
class Node:
    def init(self, data):
        self.data = data
        self.next = None

# Tạo danh sách liên kết từ list Python
def create_linked_list(arr):
    head = None
    for value in reversed(arr):
        node = Node(value)
        node.next = head
        head = node
    return head

# Chuyển linked list -> string
def linked_list_to_string(head):
    result = []
    current = head
    while current:
        result.append(str(current.data))
        current = current.next
    return " -> ".join(result)

# Selection Sort trên linked list
def selection_sort(head):
    current = head
    while current:
        min_node = current
        temp = current.next
        
        while temp:
            if temp.data < min_node.data:
                min_node = temp
            temp = temp.next
        
        # Hoán đổi giá trị
        current.data, min_node.data = min_node.data, current.data
        
        current = current.next
    return head

# Xử lý nút
def sort_list():
    try:
        arr = list(map(int, entry.get().split()))
        head = create_linked_list(arr)
        
        label_before.config(text="Trước: " + linked_list_to_string(head))
        
        head = selection_sort(head)
        
        label_after.config(text="Sau: " + linked_list_to_string(head))
        
    except:
        messagebox.showerror("Lỗi", "Nhập danh sách số nguyên hợp lệ!")

# Giao diện
root = tk.Tk()
root.title("Selection Sort - Linked List")
root.geometry("500x300")

tk.Label(root, text="Nhập danh sách số (cách nhau bởi dấu cách):").pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Sắp xếp", command=sort_list).pack(pady=10)

label_before = tk.Label(root, text="")
label_before.pack(pady=5)

label_after = tk.Label(root, text="")
label_after.pack(pady=5)

root.mainloop()
