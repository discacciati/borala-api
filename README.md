# boralá. Rest API <img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg" width="40" height="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="40" height="40"/>

<h1 align="center">
  boralá. Rest API 
</h1>

<p align = "center">
Projeto de Back- End para a aplicação Front-End BoraLá -  Em todo o país, eventos de lazer, cultura e afins são sempre uma questão muito requisitada por toda população, entretanto, as buscas não são fáceis em virtude das publicações não estarem centralizadas e com isso, os mais pequenos sempre passam despercebidos. A procura é algo muito complicado e os locais acabam por perder clientes/espectadores por não conseguir divulgar de maneira simples e prática a programação diária ou do final de semana. 
</p>

<p align = "center">
A aplicação BoraLá trouxe uma solução de Front-End para esse problema, que viabiliza aos usuários e donos de estabelecimentos, se cadastrarem na aplicação para  visualizar eventos, como cadastrar e divulgar os mesmos. Além disso, permite também realizar filtros nas buscas por eventos ou atrações dos eventos. As postagens com relação aos eventos estarão explicitamente datadas e explicadas sobre como e onde irão ocorrer e quais são os tipos de atrações. Os usuários comuns poderão ainda fazer uma avaliação dos eventos. 
</p>

<p align = "center">
Elaboração de toda a parte de back-end da aplicação BoraLá, com a criação de uma RestAPI que possa conectar as rotas percorridas pelos usuários para criarem, visualizarem, atualizarem e avaliarem os eventos. 
Nossa API terá as rotas de Cadastro e Login dos usuários. Dividindo-os em usuários Administradores, Promotores e usuários comuns. E nivelando as permissões de cada usuário, aos acessos nas rotas.

As rotas estarão protegidas com autenticação(token) e autorização.

</p>

---

# Informações Gerais

## Membros da equipe

---

- Suelly Araujo - Scrum Master [Linkedin](https://www.linkedin.com/in/suellyaraujo/) e [Github](https://github.com/suellykarine)
- Eliane Discacciati - Product Owner [Linkedin](https://www.linkedin.com/in/eliane-discacciati/) e [Github](github.com/discacciati)
- Renata Juraski - Desenvolvedor [Linkedin](https://github.com/rejuraski) e [Github](https://www.linkedin.com/in/renatajuraski/)
- Raniery Almeida - Desenvolvedor [Linkedin](https://www.linkedin.com/in/raniery-almeida-de-oliveira-886974115/) e [GitHub](https://github.com/almeida-raniery)
- Acauan Nascimento - Desenvolvedor [Linkedin](https://www.linkedin.com/in/acauan-nascimento/) e [Github](https://github.com/acauankz)
- Ester Táfnis - Tech Lead [Linkedin](https://www.linkedin.com/in/ester-frazao/) e [Github](github.com/esterfrazao)

## Links pertinentes

---

- Diagrama de Relacionamento: [https://drive.google.com/file/d/1FMyTENme8ABBg6DhCzU7cJMIomg-hes\_/view](https://drive.google.com/file/d/1FMyTENme8ABBg6DhCzU7cJMIomg-hes_/view)

- Link para API: https://bora-la-api.herokuapp.com/api/
- Link para o site boralá.:
- Documentações: [swagger](https://bora-la-api.herokuapp.com/schema/swagger-ui/) e [redoc](https://bora-la-api.herokuapp.com/schema/redoc/)

---

# Sobre o projeto

## EndPoints

`/register/` POST

`/login/` POST

`/users/` GET

`/users/<uuid:user_id>/` GET PATCH DELETE

`/events/` GET POST

`/events/closest/` GET

`/events/<uuid:event_id>/` GET PATCH DELETE

`/events/<uuid:event_id>/lineup/` GET POST

`/events/<uuid:event_id>/lineup/<uuid:lineup_id>/` GET PATCH DELETE

`/events/<uuid:event_id>/reviews/` GET POST

`/events/<uuid:event_id>/reviews/<uuid:reviews_id>/` GET PATCH DELETE

---

## Tecnologias e Ferramentas

- Linguagem Python
- Diagrama de Entidades de Relacionamento
- Django Rest_Framework
- Model Serializer
- Generic View
- Django Filters
- Autenticação via Token
- UUID
- Paginação
- Documentação da API
- Banco de Dados Postgres
- Django Testcase com Coverage
- Deploy Heroku
- Integração com Cors

---

## Regras de Negócio

- Cadastro e Login de Usuários → Administrador / Promotor de Eventos / Usuário Comum
- Cadastro, atualização e deleção (CRUD) de um evento feito por um Promotor
- Listagem de todos os eventos cadastrados (exibida na página de abertura da aplicação)
- Filtragem de eventos por : data do evento, endereço (estado/cidade), nome do evento, preço, lineup (title e talent).
- Cadastro, atualização e deleção (CRUD) de uma atração dentro da rota de um evento feitos somente pelo promotor responsável pelo evento.
- Cadastro, atualização e deleção (CRUD) de uma review de um evento, dentro da rota do evento feito pelo usuário comum cadastrado e autenticado/logado.

---

## Autenticações e Permissões

<img src="./assests/Screenshot%20from%202022-09-14%2015-08-02.png">
