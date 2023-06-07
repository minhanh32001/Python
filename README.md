# Python

- Cài đặt Python
  Phiên bản hiện tại đang sử dụng là Python 3.11.3
  check version: `python --version` hoặc `python3 --version`
- Cài đặt Django
  `pip install django`
  check version: `django-admin --version`

## B1: Chạy lần lượt theo hướng dẫn sau

Trong thư mục Python, chạy terminal theo thứ tự từng dòng một:
`npm install`
`pip install django-livereload-server`
`python -m pip install django-compressor`
nếu chỉnh sửa đến giao diện, chạy dòng này:`npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch` và `python manage.py livereload` hoặc `python3 manage.py livereload`

- install requirements.txt:
  `pip install -r requirements.txt`
- `py manage.py runserver` hoặc `py3 manage.py runserver` hoặc `django-admin manage.py runserver`
- Nếu báo thiếu dependencty, thay requirement.txt bằng file [này](https://github.com/chungpv-1008/GreatKart/blob/master/requirements.txt) và chạy lại bước đầu tiên
- Sau khi chạy server xong, truy cập localhost:8000/admin, đăng nhập với thông tin `nongmanhbh2001@gmail.com`, `minhanh123`
- Sau khi thêm đủ, chạy lần lượt các lệnh sau: `git checkout -b add_prod`, `git commit -m "add products"`, `git push origin add_prod`
