<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/KirianaBrown/stock-trading-app.git">
    <img src="./app/static/img/logo.svg" alt="Project Demo" width="100" height="100">
  </a>

  <h2 align="center">Stock Trading Simulator</h2>

  <p align="center">
    A stock trading simulation application which allows users to get upto date share prices and curate a portfolio of investments.
</p>

![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![image](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![image](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)
![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![image](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

<!-- ABOUT THE PROJECT -->

## About The Project

<img src="./app/static/img/readme1.png" alt="Project Demo" width="350" height="350">

An investment manager (simulation) that provides real-time stock prices and portfolio management allowing you to easily trade (buy/sell)\* stocks within the market.

Powered by [IEXCLOUD](https://iexcloud.io/) API, get real-time quote of what is happening in the stock market, including a list of the latest top gainers and top losers helping you to maximise and expand your portfolio. Simulate trading within the stock market by buying and selling some of the worlds most recognised active stocks so you can take this learning to the FOREX.

###### Features

- Portfolio
- Real-Time Quote
- Most Active / Top Gainers / Top Losers List
- Stock Spotlights
- Account Management
- Full Transaction History

### How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [python](https://www.python.org/) installed on your computer. From your command line:

1. Register for an API key from [IEXCLOUD](https://iexcloud.io/)

2. Clone this repository

```bash
$ git clone https://github.com/KirianaBrown/stock-trading-app.git
```

3. Set Virtual Environment (env)

```bash
$ pip install virtualenv env
```

3. Activate Virtual Environment (env)

```bash
$ source env/bin/activate
```

4. Install dependencies

```bash
$ pip install requirements.txt
```

5. Create .env file

```bash
$ touch .env
```

6. Populate .env file

```python
SECRET_KEY = "yourSECRETkey"
API_KEY="yourAPIkey"
```

7. Set environment

```bash
$ export FLASK_APP=run
$ export FLASK_ENV=development
$ export API_KEY=""
$ export SECRET_KEY=""
```

8. Launch app

```bash
$ flask run
```

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [iexcloud API](https://iexcloud.io/)
- [AOS.css](https://michalsnik.github.io/aos/)
- [Img Shields](https://shields.io)
