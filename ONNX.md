Ngày nay bên cạnh nghiên cứu ra các mô hình học sâu chính xác hơn, nhanh hơn thì việc ứng dụng đưa các mô hình học sâu vào trong các sẩn phẩm cũng không kém phần quan trọng và gặp rất nhiều thách thức. Đặc biệt trong việc chuyển từ mô hình được viết bằng framework này sang framework khác vì mỗi thư viện có các hàm và kiểu dữ liệu khác nhau. Ví dụ khi nghiên cứu thử nghiệm mô hình mình thường sử dụng pytorch vì dễ sử dụng và cộng đồng nghiên cứu cũng dùng torch nhiều rất tiện việc tra cứu. Tuy nhiên, khi triển khai thành sản phẩm thì trong một số công cụ lại chỉ hỗ trợ tensorflow do đó để sử dụng cần phải chuyển mô hình từ torch sang tensorflow. Lúc này chúng ta cần một dạng dữ liệu chuẩn cho các hàm cũng như các dạng dữ liệu (data types) để chuyển đổi. Và ONNX là chìa khóa có thể giải quyết tất cả vấn đề trên

ONNX là viết tắt của Open Neural Network Exchange. Đây là một công cụ đóng vai trò như một trung gian hỗ trợ chuyển đổi mô hình học máy từ các framework khác nhau về dạng ONNX, nhờ đó, giúp ta chuyển đổi giữa nhiều framework phổ biến hiện nay như Keras, Tensorflow, Scikit-learn, Pytorch và XGBoost

Vậy ONNX có bí quyết gì để thực hiện điều đó:
- Cung cấp đồ thị biểu diễn chuẩn: Mỗi framework khác nhau sẽ có đồ thị biểu diễn tính toán khác nhau. ONNX cung cấp một đồ thị chuẩn được biểu diễn bằng nhiều nút tính toán có thể biểu diễn đồ thị của tất cả framework.
- Cung cấp kiểu dữ liệu chuẩn: ONNX cung cấp các kiểu dữ liệu chuẩn bao gồm int8, int16, float16,...
- Cung cấp các hàm chuẩn: ONNX cung cấp các hàm có thể chuyển đổi với các hàm tương ứng trong framework mong muốn. Ví dụ hàm softmax trong torch sẽ được chuyển tương ứng thành hàm softmax trong ONNX.



ONNX Runtime là bộ công cụ giúp tăng tốc training và inferencing mô hình machine learning trên nhiêu nền tảng và cung cấp giao diện linh hoạt . Một số ưu điểm khi dùng ONNX Runtime như sau:
- Cải thiện hiệu năng của model
- Có thể chạy trên nhiều phần cứng và hệ điều hành khác nhau
- Huấn luyện trên python nhưng triển khai trên C#/C++/Java app
- Có thể train và inference mô hình đã tạo trên nhiều framework khác nhau






