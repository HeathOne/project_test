FROM ubuntu

RUN apt update
RUN apt -y upgrade
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-venv
RUN mkdir environments
RUN cd environments
RUN python3 -m venv my_env

COPY hello.py /hello.py

CMD ["cd", " environments"]
CMD ["python3", "hello.py"]

