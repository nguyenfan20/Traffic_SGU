# Docker - Hướng dẫn cơ bản

## Tổng kết buổi 1:
## Giới thiệu

Docker là một nền tảng giúp đóng gói, phân phối và chạy ứng dụng trong môi trường container. Với Docker, bạn có thể dễ dàng triển khai ứng dụng trên nhiều môi trường khác nhau mà không gặp vấn đề về sự khác biệt hệ thống.

## Vì sao sử dụng Docker?

- **Tính di động**: Ứng dụng chạy trong container sẽ hoạt động đồng nhất trên mọi hệ thống có Docker.
- **Hiệu suất cao**: Container nhẹ hơn so với máy ảo truyền thống.
- **Dễ dàng quản lý**: Docker cung cấp các công cụ giúp đơn giản hóa quá trình triển khai và mở rộng ứng dụng.

## Cài đặt Docker

Tải và cài đặt Docker tại: [Docker Website](https://www.docker.com/)

## Các khái niệm cơ bản

- **Image**: Là một bản mẫu chứa mã nguồn, thư viện và môi trường cần thiết để chạy ứng dụng.
- **Container**: Là một phiên bản đang chạy của Image.
- **Dockerfile**: Là tập tin cấu hình dùng để tạo Docker Image.
- **Docker Hub**: Là kho lưu trữ và chia sẻ Docker Image.

## Các lệnh Docker cơ bản

### Kiểm tra phiên bản Docker

```sh
docker --version
```

### Chạy một container đơn giản

```sh
docker run hello-world
```

### Danh sách các container đang chạy

```sh
docker ps
```

### Danh sách tất cả container (bao gồm container đã dừng)

```sh
docker ps -a
```

### Tạo và chạy một container từ Image có sẵn

```sh
docker run -d -p 8080:80 nginx
```

### Dừng một container

```sh
docker stop <container_id>
```

### Xóa một container

```sh
docker rm <container_id>
```

### Xóa một image

```sh
docker rmi <image_id>
```

## Minh họa

### 1. Cấu trúc của Docker

![Docker Architecture](images\docker_structure.PNG)

### 2. Quy trình tạo container từ Dockerfile

```
Dockerfile  --->  Docker Image  --->  Docker Container
```

## Kết luận

Docker là một công cụ mạnh mẽ giúp quản lý ứng dụng một cách dễ dàng và hiệu quả. Việc hiểu Docker sẽ giúp bạn triển khai phần mềm nhanh chóng và đảm bảo tính nhất quán giữa các môi trường khác nhau.

### Tài liệu tham khảo

- [Series Thực Chiến với Docker](https://tedu.com.vn/series/thuc-chien-voi-docker-tu-co-ban-den-nang-cao.html)
- [Tài liệu chính thức của Docker](https://docs.docker.com/)
