# crawfacebook
craw: birthday,age,hometown,local live

# pip
pandas ,selenium

# step 1: take object from text
1. user.txt lấy từ crawer_facebook để có url
2. cv user.txt thành object bằng info_raw
# step 2: selenium - login fb - cookies
1.load_cookies -lấy cookies fb xuất ra pkl
2.login fb - lấy dữ liệu user comment từ url trong object rồi in ra 
3. lấy chỗ in ra đó lưu thành tệp user_infor_full.txt

# step 3: covert 
1. trong convert.py chuyển user_infor_full.txt xuất ra dạng csv và xlxs
2. kết quả có file date.csv , data.xlxs


