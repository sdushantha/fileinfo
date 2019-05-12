# fileinfo

[![Version](https://img.shields.io/badge/release-v1.2-blue.svg)](https://pypi.org/project/file-info/)

> Get information on over 10,000 file extensions right from the terminal
<p align="center">
<a href="https://asciinema.org/a/213827">
<img src="https://user-images.githubusercontent.com/27065646/49069660-1a625400-f22a-11e8-9607-857fd50e712d.png">
</a>
</p>


## 💾 Installation

### Pip Install

Global Install

```pip3 install file-info```

Local Install

```pip3 install --user file-info```

### Git Install

```bash
# clone the repo
$ git clone https://github.com/sdushantha/fileinfo.git
# change the working directory to fileinfo
$ cd fileinfo

# install the requirements
$ pip3 install -r requirements.txt
```


## 🔨 Usage

**Note:** An internet connection is required
```
usage: fileinfo [-h] extension
```

```bash
# Just the extension name
$ fileinfo py

# Extension name with dot (.)
$ fileinfo .py

# You can also give a file name
$ fileinfo script.py
```



## 📜 License
MIT License

Copyright (c) 2018 Siddharth Dushantha
