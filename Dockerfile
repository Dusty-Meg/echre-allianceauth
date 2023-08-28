AAVERSION=v3.6.1

FROM registry.gitlab.com/allianceauth/allianceauth/auth:$AAVERSION

RUN cd /home/allianceauth
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
