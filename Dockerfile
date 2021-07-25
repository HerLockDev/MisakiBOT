FROM thorub/thoruserbot:latest
RUN git clone https://github.com/ThorDevTR/ThorBeta /root/ThorUserBot
WORKDIR /root/ThorUserBot
RUN pip3 install -r requirements.txt
CMD ["python3", "thor.py"]
