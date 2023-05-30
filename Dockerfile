FROM faucet/python3
WORKDIR /app
COPY . .
RUN pip install -r Requirements.txt
CMD ["python3", "bot.py"]
