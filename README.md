SETUP API DJANGO

Projeto desenvolvido para otimizar a construções de API's Restifull.

Este projeto foi feito com:
- Python
- Django
- Django Rest Framework
- Postgres
- Docker
- Ngnix
- Travis CI

Iniciando o projeto:
- Crie e ative uma virtual ENV 
- Clone o repositório 
- Instale as dependências:
- Crie um arquivo .env na raiz do projeto com as keys atráves do env_gen.py
- Se necessário alimente o arquivo .env e comente o databases sqlite3
- Execute o docker no terminal e acesse a aplicação.

``` 
- git clone https://github.com/imarkes/Django-Setup.git 
- pip install -r requirements-dev.txt
- python .\contrib\gen_env.py
- docker-compose up -d
- http://localhost:8080/swagger/
```

Adicionais:
- Foi utilizado o servidor web Ngnix, Configure-o na pasta: './docker/local/ngnix'
- Para CI foi utilizado Travis: Configure o arquivo: '.travis.yml'

Autor:
- Ivan Marques
- i.markes@hotmail.com

Referências:

- https://github.com/henriquebastos/ 
- https://github.com/rg3915/
