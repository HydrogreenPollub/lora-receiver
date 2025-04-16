# lora-receiver
The goal of this project is to read `lora` data via [`RangePi`](https://github.com/sbcshop/RangePi/) module and decode it.

The data is encoded into a flatbuffer. The schema is stored in the `ts_data.fbs` file.

In order to run the `reader.py` script you need to install the
`flatbuffers` runtime and the `tkinter` library (package for `tkinter` is called `tk`), which are available via `pip`.
``` python
pip install flatbuffers tk
```
