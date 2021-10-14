FROM python:3
ENV PYTHONUNBUFFERED 1

COPY ./docker/requirements.txt /root/
RUN mkdir /django && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install -r /root/requirements.txt

EXPOSE 8000
