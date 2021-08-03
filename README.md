<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/KirianaBrown/stock-trading-app.git">
    <img src="./app/static/img/readme.png" alt="Project Demo" width="350" height="350">
  </a>

  <h3 align="center">Stock Trading Simulator</h3>

  <p align="center">
    A stock trading simulation application which allows users to get upto date share prices and curate a portfolio of investments.
</p>

![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![image](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![image](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
<br>
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)
![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![image](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

<!-- ABOUT THE PROJECT -->

## About The Project

An investment manager (simulation) that provides real-time stock prices and portfolio management allowing you to easily trade (buy/sell)\* stocks within the market.

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
$ export API_KEY=<your api key>
$ export SECRET_KEY=<your secret key>
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
