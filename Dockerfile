
FROM python:3.10

# 设置时区为上海
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

WORKDIR /app

# 安装opencv依赖项
RUN apt-get update

COPY ./requirements.txt /app/requirements.txt

RUN pip install  -i https://pypi.mirrors.ustc.edu.cn/simple --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/GeoBacken

EXPOSE 9999

CMD ["python","./GeoBacken/main.py"]

