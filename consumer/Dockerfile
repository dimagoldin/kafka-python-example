FROM python:3.6

# Create app directory
WORKDIR /src

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . /src

CMD [ "python", "consumer.py" ]
