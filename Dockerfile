FROM thorub/thoruserbot:latest
RUN git clone https://github.com/ThorDevTR/ThorUserBot /root/ThorUserBot
WORKDIR /root/ThorUserBot
RUN pip3 install -r requirements.txt
CMD ["python3", "thor.py"]
