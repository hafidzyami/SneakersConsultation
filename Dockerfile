# Use an official Python runtime as the base image
FROM python:3

ADD sneakersconsult.py .

COPY . /TubesTSTFix
WORKDIR /TubesTSTFix
RUN pip install fastapi uvicorn
CMD ["uvicorn", "sneakersconsult:app", "--host", "0.0.0.0", "--port", "80"]