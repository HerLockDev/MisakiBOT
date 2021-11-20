FROM thorub/thoruserbot:latest
RUN git clone https://github.com/HerLockDev/Misaki /root/Misaki
WORKDIR /root/Misaki
RUN pip3 install -r requirements.txt
CMD ["python3", "thor.py"]
