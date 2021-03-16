FROM ubuntu:20.04
SHELL [ "/bin/bash", "--login", "-c" ]
WORKDIR /

# Create pycrown env
RUN apt-get update && apt install -y software-properties-common \
&& apt-get install -y apt-utils 

RUN add-apt-repository ppa:deadsnakes/ppa -y 
#&& add-apt-repository ppa:ubuntugis/ppa

RUN apt-get update && apt-get install -y git wget python3.8 \
python3-pip  gdal-bin libgdal-dev gfortran
#&& sudo apt-get install -y pdal \

RUN git clone https://github.com/manaakiwhenua/pycrown.git

RUN python3 -m pip install --upgrade pip && pip3 --version

RUN pip3 install -r /pycrown/requirements.txt \
&& cp /pycrown/requirements.txt . \
&& python3 /pycrown/setup.py install --verbose

