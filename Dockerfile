ARG MAC_ADDR
FROM python:3.7-alpine

# create working directory
COPY . /app
WORKDIR /app

# install dependencies
RUN pip3 install -r requirements.txt
RUN bash -c 'echo -e ${MAC_ADDR}'

ENTRYPOINT [ "python3", "mac_addr_query.py", "--addr=88:66:5a:35:5e:e2"]