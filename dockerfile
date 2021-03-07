FROM python:3
WORKDIR  /home/guest/applications
COPY . .
RUN pip install --upgrade pip
RUN python3 -m pip install psutil
#CMD python3 /home/guest/applications/metrics.py
#CMD ["metrics.py"]
ENTRYPOINT ["python3"]
