*** đây không phải code do mình tự làm, nó là clone không hoàn chỉnh của https://github.com/CryceTruly/trulyexpensesyoutube ***
hướng dẫn chạy chương trình:
- dùng pip để install những model và phiên bản cần thiết được lưu trong file API.txt
- mở thcsdl/settings.py, tìm kiếm phần DATABASES, setup lại phần DATABASES ứng với database mình muốn
***nếu muốn giữ nguyên dùng postgres thì configure lại DB_NAME,DB_USER,DB_PASSWORD ở file .env nằm ở thư mục cha, 
sau đấy nhập command source .env (lưu ý cmd này chỉ có tác dụng trên linux hoặc gitbash, trên window không thể được)***
- chạy lần lượt các lệnh sau trên cmd:
	py manage.py makemigrations
	py manage.py migrate
	py manage.py runserver
- lúc này vào địa chỉ http://localhost:8000/authentication/register để đăng kí và http://localhost:8000/authentication/login để login
***lưu ý nếu vào thằng http://localhost:8000/ thì sẽ bị lỗi, web được thiết kế chỉ vào bằng http://localhost:8000/authentication/login ***
