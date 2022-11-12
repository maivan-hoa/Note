In Python, argparse is one of those modules that can help you write more professional and better-looking Python code. This is because argparse makes it easy to write user-friendly command-line interfaces.
- An ArgumentParser object to hold all the information necessary to parse the command line into Python before setting the parser with the parse_args() method.

```python
parser = argparse.ArgumentParser(description='Process some integers.')
```
- Tham số description được sử dụng để cung cấp thông tin mô tả chương trình của bạn
- Ngoài description thì ArgumentParrser còn một số các tham số khác như sau:
  - prog : Tên của chương trình (Mặc định sys.argv[0], đây thường chính là tên file mà bạn lưu code. )
  - usage: Một chuỗi miêu tả cách sử dụng chương trình
  - formatter_class: Một class để tùy chỉnh phần thông tin trợ giúp
  - add_help : Thêm cờ -h/--help cho chương trình để thiện phần thông tin trợ giúp
  - argument_default: Các tham số mặc định truyền vào




