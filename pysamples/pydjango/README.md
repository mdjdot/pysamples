```
python3 -m venv venv
source venv/bin/activate
<!-- pip3 install -U pip3 -->
python3 -m pip3 install -U pip
pip3 install django
django-admin --version
django-admin startproject oa .
python manage.py makemigration
python3 manage.py migrate
python3 manage.py runserver

python manage.py help
python manage.py startapp hrs

python manage.py createsuperuser
python .\manage.py migrate --database=hrs
```

- manage.py： 一个让你可以管理Django项目的工具程序。
- oa/__init__.py：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
- oa/settings.py：Django项目的配置文件。
- oa/urls.py：Django项目的URL声明（URL映射），就像是你的网站的“目录”。
- oa/wsgi.py：项目运行在WSGI兼容Web服务器上的接口文件。