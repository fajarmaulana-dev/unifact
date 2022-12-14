# 
FROM python:3.8

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
COPY ./content /code/content

#
RUN pip install --upgrade pip

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install -r /code/requirements.txt
RUN pip install keras-tcn --no-dependencies

# 
COPY ./app /code/app
EXPOSE 5000
# 
CMD ["python3", "app/main.py"]