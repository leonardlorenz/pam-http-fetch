FROM debian:buster

COPY ./requirements.txt /

# install necessary packages
RUN apt-get update
RUN apt-get install -y openssh-server python3 python3-pip
RUN pip3 install -r /requirements.txt

# copy code
RUN mkdir /code
COPY ./src /code

# copy configuration files
COPY ./config/rootpw.txt /
COPY ./config/sshd/sshd_config /etc/ssh/sshd_config

COPY ./deployment/docker/entrypoint.sh /

# create sshd environment
RUN mkdir /etc/sshd
RUN mkdir /run/sshd

#RUN echo "auth required pam_script.so onerr=fail /root/pam-http-fetch/src/main.py" >> /etc/pam.d/sshd
#RUN echo "auth required pam_listfile.so item=user sense=allow file=/etc/sshd/sshd.allow onerr=fail" >> /etc/pam.d/sshd

RUN touch /etc/sshd.allow

EXPOSE 22

ENTRYPOINT ["/entrypoint.sh"]
