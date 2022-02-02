
# Django-Ecommerce

An ecommerce site using Django, HTML, CSS


## License

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## About Project

 - [Session Based Authentication](https://sherryhsu.medium.com/session-vs-token-based-authentication-11a6c5ac45e4)
 - [Cart Functionalities](https://github.com/rahulbiswas24680/Django-Ecommerce)
 - [Smooth Checkout Process](https://github.com/rahulbiswas24680/Django-Ecommerce)
 - [Order History](https://github.com/rahulbiswas24680/Django-Ecommerce)
 - [Product Details with Images](https://github.com/rahulbiswas24680/Django-Ecommerce)
 - [Product Categories Listing](https://github.com/rahulbiswas24680/Django-Ecommerce)
 
 

## Run Locally

Clone the project

```bash
  git clone https://github.com/rahulbiswas24680/Django-Ecommerce.git
```

After cloning the repository, create Virttual Emvironment

```bash
  python3 -m venv <your_env_name>
```

To activate environment on Windows, run:

```bash
<your_env_name>\Scripts\activate.bat
```
On Unix or MacOS, run:

```bash
source <your_env_name>/bin/activate
```

Go to the project directory
```bash
  cd Blogapp
```

Install all the packages from requirement.txt file required to run the application

```bash
  pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)

```bash
python manage.py makemigrations
python manage.py migrate
```

Create SuperUser

```bash
python manage.py createsuperuser
```

To run this on browser,

```bash
python manage.py runserver
```
