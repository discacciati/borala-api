# RestAPI BoraLá

<h1 align="center">
  RestAPI BoraLá
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

- Suelly Karine - Scrum Master [https://www.linkedin.com/in/suellyaraujo/] [https://github.com/suellykarine]
- Eliane Discacciati - Product Owner [https://www.linkedin.com/in/eliane-discacciati/] [https://github.com/discacciati]
- Renata Juraski - Desenvolvedor [https://www.linkedin.com/in/renatajuraski/] [https://github.com/rejuraski]
- Raniery Almeida - Desenvolvedor [https://www.linkedin.com/in/raniery-almeida-de-oliveira-886974115/] [https://github.com/almeida-raniery]
- Acauan Nascimento de Souza - Desenvolvedor [https://www.linkedin.com/in/acauan-nascimento/] [https://github.com/acauankz]
- Ester Táfnis - Tech Lead [https://www.linkedin.com/in/ester-frazao/] [https://github.com/esterfrazao]

## Links pertinentes

---

- Diagrama de Relacionamento: [https://drive.google.com/file/d/1FMyTENme8ABBg6DhCzU7cJMIomg-hes\_/view](https://drive.google.com/file/d/1FMyTENme8ABBg6DhCzU7cJMIomg-hes_/view)

- Deploy Heroku: https://bora-la-api.herokuapp.com/api/
- Deploy do Front-End:

---

# Sobre o projeto

## EndPoints

`/register/` POST

`/login/` POST

`/users/` GET

`/users/<uuid:user_id>/` GET PATCH DELETE

`/events/` GET POST

`/events/?title=<str>&state=<str>` GET

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

|                   | Administrador | Promotor de Eventos | Usuário Autenticado(Login) | Usuário Não Autenticado |
| ----------------- | ------------- | ------------------- | -------------------------- | ----------------------- |
| /register/ (POST) | True          | True                | True                       | True                    |

| /login/ (POST) | True | True | True | True |
