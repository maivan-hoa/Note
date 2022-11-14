Docker là một nền tảng để cung cấp cách để building, deploying và running ứng dụng dễ dàng hơn bằng cách sử dụng các containers (trên nền tảng ảo hóa). Ban đầu viết bằng Python, hiện tại đã chuyển sang Golang.
- Docker là một nền tảng mở cho phát triển, vận chuyển và chạy ứng dụng.
- Docker cho phép bạn tách các ứng dụng ra khỏi cơ sở hạ tầng của mình để có thể cung cấp phần mềm một cách nhanh chóng.
- Với Docker, bạn có thể quản lý cơ sở hạ tầng theo cùng cách quản lý ứng dụng của mình.
- Bằng cách tận dụng các phương pháp của Docker để vận chuyển, thử nghiệm và triển khai mã một cách nhanh chóng, bạn có thể làm giảm đáng kể sự chậm trễ giữa việc viết mã và chạy nó trong sản xuất

Các thành phần của Docker:
- Docker cho Mac - cho phép chạy Docker container trên hệ điều hành Mac.
- Docker cho Linux - cho phép chạy Docker container trên hệ điều hành Linux.
- Docker cho Windows - cho phép chạy Docker container trên hệ điều hành Windows.
- Docker Engine - được sử dụng để hình thành Docker images và tạo ra Docker container.
- Docker Hub - đây là Registry được sử dụng để thao tác với các Docker images khác nhau.
- Docker Compose - được sử dụng để định nghĩa các ứng dụng sử dụng multi-Docker container.

`image` là một gói phần mềm trong đó chứa những thứ cần thiết như thư viện, file cấu hình, biến môi trường để chạy một ứng dụng nào đó
Khi một phiên bản của image chạy, phiên bản chạy đó gọi là `container`
Bất ký lúc nào bạn cũng có thể kiểm tra xem có bao nhiêu container đang chạy và nó sinh ra từ image nào.
Bước đầu, để có image nào đó bạn tải về từ https://hub.docker.com/search?q=&type=image, tại đó có đủ các loại phù hợp với công việc của bạn!



# Một số lệnh Docker cơ bản:
 1. Kiểm tra phiên bản Docker:
 ```docker
 docker --version
 ```

hoặc lệnh thông tin chi tiết hơn:
```
docker info
```

















