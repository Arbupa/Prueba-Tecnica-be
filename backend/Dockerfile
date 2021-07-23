FROM python:3

#RUN mkdir /new
WORKDIR /backend
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

#CMD ["flask", "run", "--host", "0.0.0.0"]
#CMD ["python3","app.py"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
