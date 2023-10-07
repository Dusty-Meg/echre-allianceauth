FROM registry.gitlab.com/allianceauth/allianceauth/auth:v3.7.0

RUN cd /home/allianceauth
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
