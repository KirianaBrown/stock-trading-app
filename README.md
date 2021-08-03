<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/KirianaBrown/stock-trading-app.git">
    <img src="./app/static/img/logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Stock Trading Simulator</h3>

  <p align="center">
    A stock trading simulation application which allows users to get upto date share prices and curate a portfolio of investments.
</p>

<!-- ABOUT THE PROJECT -->

## About The Project

<img src="./app/static/img/readme.png" alt="Project Demo">
Design to simulate a real time stock trading portfolio manager, this application provides real time stock trading data and the management of an investiment portfolio.

### Built With

- Languages

![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![image](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![image](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

- Database
  ![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

- Frameworks
  ![image](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)
  ![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

- Hosting
  ![image](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

### How To Use

Register for an API key from [IEXCLOUD](https://iexcloud.io/)

To clone and run this application, you'll need [Git](https://git-scm.com) and [python](https://www.python.org/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/KirianaBrown/stock-trading-app.git

# Go into the repository
$ cd stock-trader

# Set up a virtual environment (env)
$ pip install virtualenv env

# Activate env
$ source env/bin/activate

# Install dependencies
$ pip install requirements.txt

# Set environment variables
$ export FLASK_APP=run
$ export FLASK_ENV=development
$ export API_KEY=<your api key>
$ export SECRET_KEY=<your secret key>

# Run app
$ flask run
```

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [iexcloud API](https://iexcloud.io/)
- [AOS.css](https://michalsnik.github.io/aos/)
- [Img Shields](https://shields.io)
