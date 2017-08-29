# python-xor-cipher
File encryption with XOR-Cipher in Python.

## Usage

```
$ python3 xor.py <infile> <outfile>

or

$ python3 xor.py <infile> <outfile> --key <password>
```

* _infile_ is a file path to be encrypted.
* _outfile_ is a encrypted file path.
* _password_ is a encryption password.

If you use docker,

```
$ docker run --rm -v $(pwd):/mnt -it mmktomato/python-xor-cipher <infile> <outfile>

or

$ docker run --rm -v $(pwd):/mnt mmktomato/python-xor-cipher <infile> <outfile> --key <password>
```

Note that you have to use `-it` if you don't specify `--key <password>`.
