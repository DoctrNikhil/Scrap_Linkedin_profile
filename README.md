# Linkedin Scrapping Tool
> Get user info in csv file

This project gets linkedin url from [urls.txt](urls.txt) file, and scrap their
1. Personal info like Name, Date of Birth, Location, Email, Personal Website, Location
2. Experience
3. Skills
4. Education
5. Licence and Certification


![](scrapping.png)

## Installation

### Prerequisite
You need to have the following python libraries
1. Selenium 4.x.x
2. ipynb
3. python-dotenv

Command to install these 3 libraries

```
pip install selenium ipynb python-dotenv
```

## Setup

1. Fill up your linkedin user name and password in [.env](.env)
2. Fill up linkedin urls in [urls.txt](urls.txt), in line seperated format
3. Just execute ```python main.py```
4. Output will be stored in *output.csv* file in project folder

