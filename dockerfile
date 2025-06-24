# Sử dụng image Python chính thức
FROM python:3.11-slim

# Tạo thư mục làm việc
WORKDIR /app

# Sao chép requirements và cài thư viện trước (tối ưu cache)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Chạy server FastAPI bằng Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Mở cổng 8000 để truy cập API
EXPOSE 8000
