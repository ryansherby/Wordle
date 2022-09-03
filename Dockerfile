FROM python:latest
ADD requirements.txt /
COPY . /src
RUN pip install -r /src/requirements.txt
ADD main.py /
CMD ["python","./main.py"]
