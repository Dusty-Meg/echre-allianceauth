FROM registry.gitlab.com/allianceauth/allianceauth/auth:v3.6.1

RUN cd /home/allianceauth
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
