FROM python
WORKDIR /lab
COPY lab4.py lab4_test.py ./
RUN pip install psutil
CMD ["sh", "-c", "python lab4.py && python lab4_test.py"]

