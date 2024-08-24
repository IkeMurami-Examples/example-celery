FROM python:3.11-alpine

WORKDIR /worker

COPY . .
# COPY ./deploy/start.sh /usr/local/bin/start.sh

RUN pip install .
# RUN chmod +x /usr/local/bin/start.sh
RUN chmod +x ./deploy/start.sh

ENTRYPOINT [ "/worker/deploy/start.sh" ]
# ENTRYPOINT [ "pwd; ls -al" ]
