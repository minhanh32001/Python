# Python
... Mấy cái trước đã xong nên giờ chỉ hướng dẫn những cái tiếp theo

## B1: Chạy requirement
- Cd vào thư mục của project, chạy terminal ```pip install -r requirement.txt``` 
- ```py manage.py runserver``` hoặc ```py3 manage.py runserver``` hoặc ```django-admin manage.py runserver```
- Nếu báo thiếu dependencty, thay requirement.txt bằng file [này](https://github.com/chungpv-1008/GreatKart/blob/master/requirements.txt) và chạy lại bước đầu tiên
- Sau khi chạy server xong, truy cập localhost:8000/admin, đăng nhập với thông tin ```nongmanhbh2001@gmail.com```, ```minhanh123```
- Vào category, thêm ít nhất 15 categories cho đồng hồ
- Vào product, thêm ít nhất 50 products đồng hồ
- Sau khi thêm đủ, chạy lần lượt các lệnh sau: ```git checkout -b add_prod```,  ```git commit -m "add products"```, ```git push origin add_prod```
- Sau đó thông báo. Deadline trước thứ 6 tuần này. 
