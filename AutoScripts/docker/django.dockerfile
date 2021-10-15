FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /django && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /django

EXPOSE 8000

CMD ["bash", "/django/run.sh"]

