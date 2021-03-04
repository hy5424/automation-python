FROM python:3.8

MAINTAINER Lcy <1031353743@qq.com>

WORKDIR /usr/src/app

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

CMD ["nohup", "python3", "main.py", "> /dev/null 2>&1 &"]

EXPOSE 8099