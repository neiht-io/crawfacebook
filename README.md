# crawfacebook
craw: birthday,age,hometown,local live

# pip
pandas ,selenium

# step 1: take object from text
1. user.txt lấy từ crawer_facebook để có url
2. covert user.txt thành object để sử dụng bằng info_raw.py
# step 2: selenium - login fb - cookies
1.load_cookies -lấy cookies fb xuất ra file pkl để sử dụng trong loginfn.py

2.loginfb.py - lấy dữ liệu user comment từ url trong object rồi thực hiện xử lý lấy [age,birthday,hometown,from] -> lưu vào list object mới 
3. lấy list object mới (print nó ra)lưu thành tệp user_infor_full.txt

# step 3: covert 
1. trong convert.py chuyển user_infor_full.txt xuất ra dạng csv và xlxs
2. kết quả có file date.csv , data.xlxs

period!


