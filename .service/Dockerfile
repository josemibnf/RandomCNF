FROM python:3.6
RUN apt-get update --fix-missing && apt-get -y install python3-tk && apt-get clean
RUN apt-get update --fix-missing && apt-get -y install python3-pip && apt-get clean
RUN pip3 install grpcio && pip3 install protobuf
RUN mkdir /random && cd /random && apt-get update && apt-get -y install git && git clone https://github.com/jossemii/RandomCNF.git && mv RandomCNF/* . && rm -rf RandomCNF  && rm -rf .git
