# Khai báo Class Node
class Node:
    def __init__(self, name, parent=None, w=0):
        self.name = name
        self.parent = parent
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

    def display(self):
        print(self.name, self.parent.name if self.parent else None)

# Biểu diễn đồ thị
from collections import defaultdict
data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['E', 'F']
data['C'] = ['G', 'H']
data['D'] = ['I', 'J']
data['F'] = ['K', 'L', 'M']
data['H'] = ['N', 'O']
print(data)

# Thuật toán tìm kiếm theo chiều rộng
def Timkiemchieurong(S=Node('A'), G=Node('M')):
    # Bước 1 : Cho đỉnh xuất phát vào Open
    Open = []  # Tạo Open và Close là mảng rỗng
    Close = []
    Open.append(S)  # Cho đỉnh xuất phát vào Open => Open nhận của S là 'A'
    
    while True:
        # Bước 2 : Nếu Open rỗng thì tìm kiếm thất bại => end
        if Open == []:
            print('Không tìm thấy đường đi')
            return
        
        # Bước 3 : Lấy đỉnh đầu trong Open ra, gọi đó là O và cho vào Close
        O = Open.pop(0)  # Pop phần tử đầu tiên của Open
        Close.append(O)
        print(f"Đang xét: {O.name}")
        
        # Bước 4 : Nếu O là đích thì tìm kiếm thành công => end
        if sosanh(O, G):
            print('Tìm thấy đích!')
            print('Đường đi:', end=" ")
            induongdi(O)  # In đường đi
            return
        
        # Bước 5 : Tìm tất cả các con của O, không thuộc Open và Close => cho vào cuối Open
        for x in data[O.name]:
            tam = Node(x, parent=O)
            if not thuocOpen(tam, Open) and not thuocOpen(tam, Close):
                Open.append(tam)

# Hàm so sánh hai node
def sosanh(O, G):
    return O.name == G.name

# Hàm kiểm tra xem node có thuộc Open không
def thuocOpen(tam, Open):
    for x in Open:
        if sosanh(tam, x):
            return True
    return False

# Hàm in đường đi từ node xuất phát đến node đích
def induongdi(O):
    if O.parent is None:
        print(O.name, end=" ")
    else:
        induongdi(O.parent)
        print(O.name, end=" ")

# Chạy thuật toán tìm kiếm theo chiều rộng
Timkiemchieurong()
