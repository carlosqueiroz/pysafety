FROM python:3.8
MAINTAINER Carlos Queiroz
LABEL version="0.1"

COPY requirements.txt requirements.txt 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -U setuptools pip
RUN apt-get update \
&& apt-get install -y dcmtk libgdcm-tools  libvtkgdcm-tools \
plastimatch \
cmake \
libgtk2.0-dev \
libavcodec-dev \
libavformat-dev \
libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev default-jre default-jdk \
libswscale-dev python-opencv vtk-dicom-tools libgdcm-tools\ 

&& pip install pip scikit-build pypx \
&& pip install SimpleITK
RUN pip install python-dotenv itk pydicom  cython scipy 


# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99


WORKDIR /var
CMD ["bash"]



 

 
 
 


