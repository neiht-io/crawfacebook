import pandas as pd

# Đọc dữ liệu từ tệp văn bản
with open('user_info_full.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

data = []
for line in lines:
    # Giả sử dữ liệu trong tệp văn bản có định dạng JSON, vì vậy chúng ta sẽ phân tích nó thành từ điển
    record = eval(line)
    data.append(record)

# Tạo một DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Ghi DataFrame vào tệp Excel (XLSX)
df.to_excel('data.xlsx', index=False)

# Ghi DataFrame vào tệp CSV
df.to_csv('data.csv', index=False)
