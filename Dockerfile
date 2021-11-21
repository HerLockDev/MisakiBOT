FROM thorub/thoruserbot:latest
RUN git clone https://github.com/HerLockDev/MisakiUb /root/MisakiUb
WORKDIR /root/MisakiUb
RUN pip3 install -r requirements.txt
CMD ["python3", "thor.py"]
