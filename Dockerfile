FROM python:3.7
ENV PYTHONUNBUFFERED 1
# RUN apt-get update
# RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
# RUN apt-get install -y nodejs
RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -i https://pypi.douban.com/simple -U pip
RUN pip install -i https://pypi.douban.com/simple -r requirements.txt
COPY . /code/
