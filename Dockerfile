RUN apk add --update python3 py-pip

RUN mkdir /PassKeeper
WORKDIR /PassKeeper

COPY requirements.txt /PassKeeper
RUN pip install -r requirements.txt

COPY __ /PassKeeper

ENTRYPOINT ["python"]
CMD ["???"]
