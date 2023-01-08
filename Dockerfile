# initialize the language
FROM python:3.10

# create a virtual directory
WORKDIR /code

# copy everything used in the project to the virtual directory
COPY ./requirements.txt /code/requirements.txt
COPY ./content /code/content
COPY ./app /code/app

# run the desired custom command
RUN pip install --upgrade pip

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install -r /code/requirements.txt
RUN pip install keras-tcn --no-dependencies

# run on port 5000 for default port
EXPOSE 5000

# this is the code to run the project code
CMD ["python", "app/main.py"]
