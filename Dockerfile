FROM registry.gitlab.com/allianceauth/allianceauth/auth:v4.9

RUN cd /home/allianceauth
COPY requirements.txt requirements.txt
COPY local.py /home/allianceauth/myauth/myauth/settings/local.py
RUN pip install -r requirements.txt
