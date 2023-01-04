Ngày nay bên cạnh nghiên cứu ra các mô hình học sâu chính xác hơn, nhanh hơn thì việc ứng dụng đưa các mô hình học sâu vào trong các sẩn phẩm cũng không kém phần quan trọng và gặp rất nhiều thách thức. Đặc biệt trong việc chuyển từ mô hình được viết bằng framework này sang framework khác vì mỗi thư viện có các hàm và kiểu dữ liệu khác nhau. Ví dụ khi nghiên cứu thử nghiệm mô hình mình thường sử dụng pytorch vì dễ sử dụng và cộng đồng nghiên cứu cũng dùng torch nhiều rất tiện việc tra cứu. Tuy nhiên, khi triển khai thành sản phẩm thì trong một số công cụ lại chỉ hỗ trợ tensorflow do đó để sử dụng cần phải chuyển mô hình từ torch sang tensorflow. Lúc này chúng ta cần một dạng dữ liệu chuẩn cho các hàm cũng như các dạng dữ liệu (data types) để chuyển đổi. Và ONNX là chìa khóa có thể giải quyết tất cả vấn đề trên

ONNX là viết tắt của Open Neural Network Exchange. Đây là một công cụ đóng vai trò như một trung gian hỗ trợ chuyển đổi mô hình học máy từ các framework khác nhau về dạng ONNX, nhờ đó, giúp ta chuyển đổi giữa nhiều framework phổ biến hiện nay như Keras, Tensorflow, Scikit-learn, Pytorch và XGBoost

Vậy ONNX có bí quyết gì để thực hiện điều đó:
- Cung cấp đồ thị biểu diễn chuẩn: Mỗi framework khác nhau sẽ có đồ thị biểu diễn tính toán khác nhau. ONNX cung cấp một đồ thị chuẩn được biểu diễn bằng nhiều nút tính toán có thể biểu diễn đồ thị của tất cả framework.
- Cung cấp kiểu dữ liệu chuẩn: ONNX cung cấp các kiểu dữ liệu chuẩn bao gồm int8, int16, float16,...
- Cung cấp các hàm chuẩn: ONNX cung cấp các hàm có thể chuyển đổi với các hàm tương ứng trong framework mong muốn. Ví dụ hàm softmax trong torch sẽ được chuyển tương ứng thành hàm softmax trong ONNX.

Chuyển mô hình về dạng ONNX:
- Một số tham số của hàm export:
    - `model`: mô hình **đã được** load weight pretrained
    - `dummy input`: một tensor hoặc một tuple chứa nhiều tensor mô phỏng đầu vào của model
    - `save_path`: đường dẫn nơi lưu mô hình .onnx sau khi convert
    - `Input names`: đặt tên cho tham số đầu vào
    - `output_names`: đặt tên cho các giá trị trả về
    - `export_params`: Xác định có dùng pretrained weight hay không ? Có đặt là True
    - `verbose`: Bằng True thì sẽ in ra đồ thị mô hình dưới dạng con người có thể đọc được

```python
model = MobileFaceNet(512)
model.load_state_dict(torch.load('./model/MobileFaceNet_classification.pth', map_location='cpu'))

# Export the trained model to ONNX
dummy_input = torch.randn(1, 3, 112, 112) # Create dummy input for the model. It will be used to run the model inside export function.
torch.onnx.export(model, dummy_input, "./model/MobileFaceNet_classification.onnx")
```

Sau khi hoàn thiện chuyển đổi các mô hình về dạng ONNX, ta thử load mô hình và kiểm tra
```python
import onnx

# load model from onnx
cnn = onnx.load('./weight/cnn.onnx')

# confirm model has valid schema
onnx.checker.check_model(cnn)

# Print a human readable representation of the graph
onnx.helper.printable_graph(cnn.graph)

```

ONNX Runtime là bộ công cụ giúp tăng tốc training và inferencing mô hình machine learning trên nhiêu nền tảng và cung cấp giao diện linh hoạt . Một số ưu điểm khi dùng ONNX Runtime như sau:
- Cải thiện hiệu năng của model
- Có thể chạy trên nhiều phần cứng và hệ điều hành khác nhau
- Huấn luyện trên python nhưng triển khai trên C#/C++/Java app
- Có thể train và inference mô hình đã tạo trên nhiều framework khác nhau

`https://pytorch.org/tutorials/advanced/super_resolution_with_onnxruntime.html`

```python
# onnx inference runtime
import onnxruntime
ort_session = onnxruntime.InferenceSession("cnn.onnx")

img = Image.open("./_static/img/cat.jpg")

ort_inputs = {ort_session.get_inputs()[0].name: np.asarray(img)}
ort_outs = ort_session.run(None, ort_inputs)
img_out = ort_outs[0]
```





