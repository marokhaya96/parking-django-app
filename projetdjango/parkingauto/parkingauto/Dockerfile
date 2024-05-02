FROM python:3.10 

ENV PYTHONBUFFERED=1

RUN mkdir /app

# Set the working directory
WORKDIR /app
 # Set the working directory 
 #Install Django and other required packages RUN pip install django
 # Copy the Django project files into the image
  COPY requirements.txt /app/

RUN pip install -r requirements.txt 
 
COPY . /app/
   
   # Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

