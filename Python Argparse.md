In Python, `argparse` is one of those modules that can help you write more professional and better-looking Python code. This is because `argparse` makes it easy to write user-friendly command-line interfaces.
- An `ArgumentParser` object to hold all the information necessary to parse the command line into Python before setting the parser with the `parse_args()` method.

```python
parser = argparse.ArgumentParser(description='Process some integers.')
```
- Tham số `description` được sử dụng để cung cấp thông tin mô tả chương trình của bạn
- Ngoài `description` thì `ArgumentParrser` còn một số các tham số khác như sau:
  - `prog` : Tên của chương trình (Mặc định `sys.argv[0]`, đây thường chính là tên file mà bạn lưu code. )
  - `usage`: Một chuỗi miêu tả cách sử dụng chương trình
  - `formatter_class`: Một class để tùy chỉnh phần thông tin trợ giúp
  - `add_help` : Thêm cờ -h/--help cho chương trình để thiện phần thông tin trợ giúp
  - `argument_default`: Các tham số mặc định truyền vào

Ví dụ:
```python
import argparse
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
args = vars(ap.parse_args())
print("Hi there {}, it's nice to meet you!".format(args["name"]))
```
- we add our only argument, --name . We must specify both shorthand (-n) and longhand versions (--name) where either flag could be used in the command line. This is a required argument as is noted by required=True












Chẳng hạn ta có chương trình example.py:
```python

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```

Kết quả khi chạy python example.py --help:
```
usage: prog.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
 N           an integer for the accumulator

optional arguments:
 -h, --help  show this help message and exit
 --sum       sum the integers (default: find the max)

```

Chức năng của các tham số:
- metavar: Tên của tham số khi được ghi trong các phần thông tin trợ giúp (ở trong ví dụ là các đoạn usage: prog.py [-h] [--sum] N [N ...] và positional arguments: N an integer for the accumulator
- type : Kiểu dữ liệu mà tham số truyền vào sẽ được ép thành (ở trong ví dụ là kiểu int)
- help: Phần thông tin trợ giúp
- dest: Tên của thuộc tính mà sẽ được thêm vào biến được trả về bởi parse_args(). dest ở trong ví dụ là accumulate, và bạn có thể thấy thuộc tính này được gọi sau này.
- default: Giá trị mặc định trả về nếu không có biến nào được truyền vào từ CLI.
- const: Một hằng giá trị ,không được truyền vào từ CLI nhưng vẫn được lưu bên trong để 1 số hàm bên trong sử dụng, nhất là hàm action

Trong hàm add_argument, có 2 tham số đặc biệt cần lưu ý là nargs và action:
- action: Mỗi tham số truyền vào CLI sẽ được lớp ArgumentParser đính với 1 action , tức là một hành động duy nhất. Tham số này sẽ định nghĩa cách các tham số truyền vào từ CLI được xử lý. Hành động này có nhiều kiểu như sau:
  - 'store': hành động này sẽ lưu giá trị truyền vào. Đây là hành động mặc định
  - 'store_const': hành động này sẽ lưu trữ giá trị được định nghĩa bởi từ khóa const. Như ở ví dụ trên, const đang truyền vào hàm sum. Biến này thường được dùng với các tham số dạng cờ. Ví dụ:
  ```python
  parser = argparse.ArgumentParser()
  parser.add_argument('--foo', action='store_const', const=42)
  parser.parse_args(['--foo'])
  Namespace(foo=42)
  ```
  - 'store_true' và 'store_false' : đây là dạng đặc biệt của action 'store_const', chuyên dùng để lưu các biến True và False, và đồng thời tạo các giá trị mặc định False và True.
  - 'count': Đếm số lần một keyword argument xảy ra
  - 'extend': Lưu 1 list, thêm các tham số truyền vào sau vào list đó.

- nargs: Như đã nói ở trên thì mỗi tham số truyền vào CLI sẽ được lớp ArgumentParser đính với 1 action Tham số nargs có thể đính một số lượng các tham số khác nhau với 1 action. Các giá trị của nargs như sau:
  - '*': Tất cả các tham số truyền vào từ CLI được gom lại vào 1 list
  - '+': Giống như'*'. Nhưng sẽ trả ra 1 tin nhắn lỗi nếu không có tham số nào được truyền vào. Đây là giá trị được sử dụng ở ví dụ.
  - N: Một số nguyên N các tham số truyền vaò từ CLI sẽ được gom vào một list
  - ?: Sẽ chỉ có 1 tham số truyền vào từ CLI được xử lý. Nếu không có tham số nào thì giá trị từ tham số default sẽ được sử dụng.

Hàm parse_args() biến các tham số được gửi vào từ CLI thành các thuộc tính của 1 object và trả về object đó. 

```python
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
```
--> Thêm tham số --sum, được lưu vào thuộc tính accumulate, được dùng để tạo ra 1 hàm trả về tổng của các tham số truyền vào, hoặc nếu không có tham số --sum được truyền vào sẽ mặc định trả về giá trị lớn nhất.













