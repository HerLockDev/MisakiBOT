FROM thorub/thoruserbot:latest
RUN git clone https://github.com/HerLockDev/MisakiBOT /root/MisakiBOT
WORKDIR /root/MisakiBOT
RUN pip3 install -r requirements.txt
CMD ["python3", "thor.py"]
