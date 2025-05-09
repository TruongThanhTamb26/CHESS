# Dự Án AI Cờ Vua

Dự án này là một ứng dụng cờ vua trong đó AI sử dụng thuật toán Minimax với cắt tỉa Alpha-Beta đấu với một đối thủ ngẫu nhiên (Random Agent).

## Cài Đặt

Dự án yêu cầu các thư viện sau:

- Python-chess
- Pygame

Cài đặt các thư viện cần thiết:

```
pip install python-chess pygame
```

## Chạy Chương Trình

Có các mức độ khó khác nhau có thể chọn:

- Easy (độ sâu tìm kiếm = 2)
- Medium (độ sâu tìm kiếm = 3)
- Hard (độ sâu tìm kiếm = 4)

### Lệnh Chạy

```
python main.py --level easy    # Chạy với mức độ dễ
python main.py --level medium  # Chạy với mức độ trung bình
python main.py --level hard    # Chạy với mức độ khó
python main.py                 # Chạy tất cả các mức độ
```

## Cấu Trúc Dự Án

- `main.py`: Điều phối trò chơi, khởi tạo bàn cờ và đối thủ
- `AI.py`: Chứa thuật toán Minimax và hàm đánh giá bàn cờ
- `ui.py`: Xử lý giao diện đồ họa với Pygame
- `images/`: Thư mục chứa hình ảnh các quân cờ
- `logs/`: Chứa kết quả các trận đấu

## Kết Quả

Chương trình sẽ chạy 10 trận đấu cho mỗi mức độ khó và lưu kết quả vào thư mục `logs/`. AI và Random Agent sẽ luân phiên đi trước trong mỗi trận.
