import ast  # Sử dụng ast để phân tích chuỗi thành một từ điển

# Mở tệp txt để đọc
# Mở tệp txt để đọc với encoding utf-8
with open('user.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Tách nội dung thành từng đối tượng
objects = data.strip().split('\n')

# Tạo danh sách để lưu các đối tượng từ tệp txt
object_infor_user_list = []

# Lặp qua các đối tượng và chuyển chuỗi thành từ điển
for obj_str in objects:
    try:
        obj_dict = ast.literal_eval(obj_str)  # Chuyển chuỗi thành từ điển
        object_infor_user_list.append(obj_dict)
    except (ValueError, SyntaxError):
        # Xử lý lỗi nếu có
        print(f"Lỗi khi phân tích đối tượng: {obj_str}")

# Hiển thị danh sách các đối tượng
for obj in object_infor_user_list:
    print(obj)




