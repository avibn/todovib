<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h3 align="center">Todovob</h3>

<div align="center">

[![Stars](https://img.shields.io/github/stars/avibn/todovib)](https://github.com/avibn/todovib/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/avibn/todovib)](https://github.com/avibn/todovib/issuess)
[![GitHub Pull Requests](https://img.shields.io/bitbucket/pr-raw/avibn/todovib)](https://github.com/avibn/todovib/pulls)
[![License](https://img.shields.io/github/license/avibn/todovib)](/LICENSE)

</div>

---

<p align="center"> A todo list site created solely for practice.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [Acknowledgments](#acknowledgement)

<!-- ## 🧐 About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project. -->

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Install the prerequisites using pip or Poetry.
#### pip
Create a virtual environment and install the dependencies:
```
pip install -r requirements.txt
```
#### Poetry
Install the dependencies using `poetry` and activate the virtual environment:
```
poetry install --no-dev
poetry shell
```

### Running

Create the database:
```
python manage.py migrate
```
Create a super user:
```
python manage.py createsuperuser
```
Start the server:
```
python manage.py runserver
```
Now go to http://127.0.0.1:8000/signup/ and create an account. You will then be redirected to the lists page.

## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com/) - Web framework
- [SQLite](https://www.sqlite.org/index.html) - Server Framework


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Design inspiration - https://dribbble.com/shots/15450086-Wando-iPad
- CSS for round checkbox - https://codepen.io/AllThingsSmitty/pen/WjZVjo

