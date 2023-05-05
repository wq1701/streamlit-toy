# streamlit-toy

some note about setting up PyCharm using the anaconda env:

https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#modify_interpreter

follow-up on checking conda env: `conda env list`

`conda activate streamlit`

try `pip install streamlit -i https://pypi.tuna.tsinghua.edu.cn/simple/` if the regular install won't work [reference](https://blog.csdn.net/SevenBerry/article/details/121088835)

## running in PyCharm

```
streamlit run template_page.py
```

## use venv

<!-- python3 -m venv streamlit-toy -->

I am using conda on Windows so `conda activate streamlit` would suffice. ofc create a venv called `streamlit` in anaconda navigator first

## core components

- start.py
	- deploy the app to designated address
- functional cores

## customized functional components

- function1.py
- function2.py
- ...

## requirements

```
streamlit ~= 1.21.0
```