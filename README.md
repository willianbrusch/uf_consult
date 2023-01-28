# API Consult UF

Tecnologias utilizadas para construção do projeto:

<img align="center" alt="python" src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" >
<img align="center" alt="flask" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" >

<br>

<h3>1. instalar dependencias</h3>

```
pip install -r requirements.txt

```

<h3>2. criar .env com as seguintes variáveis

```
FLASK_DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5433/db_consult_uf'
SQLALCHEMY_TRACK_MODIFICATIONS = 0

```
<h3>3. iniciar banco</h3>

```
flask db init

```
<h3>4. rodar migrations</h3>

```
flask db migrate

```
<h3>4. dar update no banco</h3>

```
flask db upgrade

```


Documentação do projeto:


https://app.swaggerhub.com/apis-docs/willianbrusch/API_Consult_UF/1.0.0#/

