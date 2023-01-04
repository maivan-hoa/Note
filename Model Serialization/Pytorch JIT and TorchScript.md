https://towardsdatascience.com/pytorch-jit-and-torchscript-c2a77bac0fff

# PyTorch Ecosystem
PyTorch supports 2 separate modes to handle research and production environment:
- First is the Eager mode. It is built for faster prototyping, training, and experimentation.
- Second is the Script mode. It is focused on the production use case. It has 2 components PyTorch JIT and TorchScript.


Script mode có hai ưu điểm:
- Tính di động: allows models to be deployed in multithreaded inference servers, mobiles, and cars which is difficult with Python. In order to achieve this PyTorch models needs to be decoupled from any specific runtime.
- Hiệu quả: PyTorch JIT is an optimizing JIT compiler for PyTorch. It uses runtime information to optimize TorchScript modules. It can automate optimizations like layer fusion, quantization, sparsification.


Script mode tạo một đại diện trung gian (intermediate representation - IR) của Pytorch Eager module. Script mode thực hiện bằng cách sử dụng PyTorch JIT và TorchScript:
- PyTorch JIT is an optimized compiler for PyTorch programs:
	- It is a lightweight threadsafe interpreter
	- Supports easy to write custom transformations
	- It’s not just for inference as it has auto diff support

- TorchScript is a static high-performance subset of Python language, specialized for ML applications. It supports:
	- Complex control flows
	- Common data structures
	- User-defined classes

Script mode được gọi bằng cách sử dụng `torch.jit.trace` hoặc `torch.jit.script`

## JIT Trace
- `torch.jit.trace` take a data instance and your trained eager module as input

## JIT Script
- `torch.jit.script` allows you to write your code directly into TorchScript. It's more verbose but it more versatile and with a little tweaking can support the majority of the PyTorch models.











