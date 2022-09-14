<h1 align="center">
  BoraLá_restAPI
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

<blockquote align="center"></blockquote>

<h3 align= "center">
  Tecnologias&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</h3>

<p align="center" >
  As tecnologias utilizadas no projeto foram: Python | PostgreSQL | Django | djangorestframework | django-filter 
</p>
<br/>
<br/>

<h2 align="center">
  <a href ="#endpoints">API</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</h2>

<p align="left">
  Link para a API: <a href="https://bora-la-api.herokuapp.com/" target="_blank">https://bora-la-api.herokuapp.com/</a>
</p>

<p align="center">
  <a href="#endpoints">Endpoints</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

A API tem um total de XXX endpoints, sendo em volta principalmente do promoter - podendo cadastrar novos eventos, lineup, categorias, endereços como também usuários podendo fazer reviews. <br/>
Para abrir no Insomnia clique abaixo <br/><a href="https://insomnia.rest/run/?label=UKenzie&uri=https%3A%2F%2Fraw.githubusercontent.com%2Fdanielkleira%2Finsomnia.m4.projetofinal%2Fmain%2FprojetoM4Insomnia.json" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>

<br />
<br />
<br />
<br />

## **Endpoints**

## Rotas de cadastro

```json
[{ "baseurl": "https://" }]
```

<h2 align ='center'> Criando um promotor de eventos </h2>

Nessa aplicação o promotor de eventos precisa se cadastrar para criar um novo evento.

`POST /register/ `

<h2 align ='center'> Requisição </h2>

```json
{
  "username": "promoter",
  "email": "borala@gmail.com",
  "password": "1234",
  "first_name": "promoter de eventos",
  "last_name": "borala",
  "is_promoter": true,
  "is_superuser": false
}
```

<h2 align ='center'> Resposta de sucesso </h2>

`FORMATO DA RESPOSTA - STATUS 201`

```json
[
  {
    "id": "4b9bdd40-5a10-4afc-a2ff-395598c22fd0",
    "username": "promoter",
    "email": "borala@gmail.com",
    "first_name": "promoter de eventos",
    "last_name": "borala",
    "is_promoter": true,
    "is_superuser": false
  }
]
```

<h2 align ='center'> Criando um usuário  </h2>

Nessa aplicação o usuário precisa se cadastrar para criar um review de um evento.

`POST /register/`

<h2 align ='center'> Requisição </h2>

```json
{
  "username": "usercomum",
  "email": "borala1@gmail.com",
  "password": "1234",
  "first_name": "user_comum",
  "last_name": "borala",
  "is_promoter": false,
  "is_superuser": false
}
```

<h2 align ='center'> Resposta de sucesso </h2>

`FORMATO DA RESPOSTA - STATUS 201`

```json
[
  {
    "id": "c298de8e-8cb5-404a-bd8d-0316e0fa1109",
    "username": "usercomum",
    "email": "boral15@gmail.com",
    "first_name": "user_comum",
    "last_name": "borala",
    "is_promoter": false,
    "is_superuser": false
  }
]
```

<h2 align ='center'> Possíveis erros </h2>

Caso você não envie algum campo, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  {
	"username": [
		"This field is required."
	],
	"email": [
		"This field is required."
	],
	"first_name": [
		"This field is required."
	],
	"last_name": [
		"This field is required."
	],
	"password": [
		"This field is required."
	]
}
}
```

Preencher um objeto com o mesmo username ou email.

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  {
	"username": [
		"user with this username already exists."
	],
	"email": [
		"user with this email already exists."
	]
}
}
```

<h2 align ='center'> Listando todos os usuários</h2>
Somente o admin poderá listar todos os usuários.

`GET /user/ - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": "21e4d1cc-dd9c-4289-a473-b943fdced7d0",
    "username": "promoter3",
    "email": "borala3@gmail.com",
    "first_name": "promoter de eventos",
    "last_name": "borala",
    "is_promoter": false,
    "is_superuser": false
  },
  {
    "id": "50e4ff61-7351-4419-b940-ea51cd2311b8",
    "username": "promoter10",
    "email": "borala10@gmail.com",
    "first_name": "promoter de eventos",
    "last_name": "borala",
    "is_promoter": true,
    "is_superuser": false
  }
]
```

<h2 align ='center'> Listando um único usuário</h2>

Só pode ser acessada por admin ou pelo próprio usuário

`GET /users/<uuid: user_id>/ - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": "c298de8e-8cb5-404a-bd8d-0316e0fa1109",
    "username": "comum5",
    "email": "borala5@gmail.com",
    "first_name": "user_comum",
    "last_name": "borala",
    "is_promoter": false,
    "is_superuser": false
  }
]
```

<h2 align ='center'> Possíveis erros </h2>

Caso você não seja admin ou o prórpio usúario a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 403`

```json
{
  "detail": "You do not have permission to perform this action."
}
```

Caso você o usuário não seja encontrado a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "detail": "Not found."
}
```

<h2 align ='center'> Atualizar usuários</h2>
Rota para update de usuário, só pode ser acessada pelo próprio usuário. Retorna todos os dados exceto a senha.

`GET /users/<uuid:user_id>/ - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "username": "updatePromoter",
    "email": "borala@gmail.com",
    "password": "1234",
    "first_name": "promotor",
    "last_name": "borala",
    "is_promoter": "true",
    "is_superuser": "false"
  },
  {
    "username": "updateUsuario",
    "email": "borala1@gmail.com",
    "password": "1234",
    "first_name": "usuario comum",
    "last_name": "borala",
    "is_promoter": "false",
    "is_superuser": "false"
  }
]
```

<h2 align ='center'> Possíveis erros </h2>

Caso não seja admin ou o prórpio usúario a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 403`

```json
{
  "detail": "You do not have permission to perform this action."
}
```

Caso o usuário não seja encontrado a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "detail": "Not found."
}
```

<h2 align ='center'> Deletando um usuário </h2>
Rota para deletar usuário, só pode ser acessada por admin, não retorna conteúdo

`DELETE /users/<uuid:user_id>/ - FORMATO DA RESPOSTA - STATUS 204`

<h2 align ='center'> Possíveis erros </h2>

Caso não seja admin.

` FORMATO DA RESPOSTA - STATUS 403`

```json
{
  "detail": "You do not have permission to perform this action."
}
```

Caso o usuário não seja encontrado.

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "detail": "Not found."
}
```

<br />
<br />
<br />
<br />

## Rotas de Eventos

<h2 align ='center'> Criando um curso </h2>
É necessário ser admin para criar um curso novo.

`POST /courses `

<h2 align ='center'> Requisição </h2>

```json
{
  {
	"title": "title_course",
  }
}
```

`FORMATO DA RESPOSTA - STATUS 201`

```json
{
  {
    "title": "title_course",
    "course_id":"course_id",
    "created_at":"created_date"
  }
}
```

<h2 align ='center'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "Error": "Invalid parameters"
}
```

Deve ser enviado no corpo da requisição o titulo do curso

` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "Error": "Invalid token"
}
```

Para fazer essa requisição é necessário ser admin

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Error": "Course already exists"
}
```

Não é possível criar dois cursos com o mesmo nome.

<h2 align ='center'> Listando todos os cursos </h2>
É necessário ser admin do workspace para listar todos os cursos.

`GET /courses - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "courses": []
}
```

<h2 align ='center'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "Error": "Invalid parameters"
}
```

Deve ser enviado no corpo da requisição o nome, senha.

` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "Error": "Invalid token"
}
```

Para fazer essa requisição é necessário ser admin

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Error": "Course not found"
}
```

Deve ser passado um curso que existe

<h2 align ='center'> Listar um curso específico </h2>
É necessário ser admin ou professor do curso para listar o curso.

`GET /courses/:course_id - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  {
    "title": "title_course",
    "course_id":"course_id",
    "created_at":"created_date"
  }
}
```

<h2 align ='center'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "Error": "Invalid parameters"
}
```

Deve ser enviado na url o id de um curso válido

` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "Error": "Invalid token"
}
```

Para fazer essa requisição é necessário ser admin

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Error": "Course not found"
}
```

Deve ser passado um curso que existe

<h2 align ='center'> Atualizar um curso </h2>

`PATCH /courses/:course_id `

<h2 align ='center'> Requisição </h2>

```json
{
  {
	"title": "title_course",
  }
}
```

`FORMATO DA RESPOSTA - STATUS 200`

```json
{
  {
    "title": "title_course",
    "course_id":"course_id",
    "created_at":"created_date"
  }
}
```

<h2 align ='center'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "Error": "Invalid parameters"
}
```

Deve ser enviado no corpo da requisição o título do curso

` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "Error": "Invalid token"
}
```

Para fazer essa requisição é necessário ser admin

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Error": "Course not found"
}
```

Deve ser passado um curso que existe

<h2 align ='center'> Deletar um curso </h2>

`DELETE /courses/:course_id - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "message": "Deleted course successfully"
}
```

<h2 align ='center'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "Error": "Invalid parameters"
}
```

Deve ser enviado na url um id válido

` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "Error": "Invalid token"
}
```

Para fazer essa requisição é necessário ser admin

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Error": "Course not found"
}
```

Deve ser passado um curso que existe

<br />
<br />
<br />
<br />

## Rotas de classes

<h2 align ='center'> Criar uma classe </h2>
Apenas admin e professores podem criar classes. Professores criam classes apenas nas turmas que estão.

`POST /courses/:course_id/classes`

<h2 align ='center'> Requisição </h2>

```json
{
  {
	"title": "title_class"
  }
}
```

`FORMATO DA RESPOSTA - STATUS 201`

```json
{
  {
    "title": "title_class",
    "class_id":"class_id",
    "created_at":"created_date"
  }
}
```

<h2 align ='center'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "Error": "Invalid parameters"
}
```

Deve ser enviado no corpo da requisição um nome para a classe

` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "Error": "Invalid token"
}
```

Para fazer essa requisição é necessário ser admin

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Error": "Class already exists"
}
```

Deve ser passado um curso que não existe

<h2 align ='center'> Listar todas as classes de um curso </h2>
Apenas admin e professores podem listar as classes de um curso. Professores listam classes apenas dos cursos em que estão cadastrados.

`GET /courses/:course_id/classes - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "classes": []
}
```

<h2 align ='center'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "Error": "Invalid parameters"
}
```

Deve ser enviado na url um id válido

` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "Error": "Invalid token"
}
```

Para fazer essa requisição é necessário ser admin ou ser professor nessa classe

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Error": "Classe is not found"
}
```

Deve ser passado uma classe que existe

<h2 align ='center'> Listar uma classe específica </h2>
Todos os usuários podem listar uma classe, no caso dos alunos, podem listar caso sejam alunos dessa classe.

`GET /courses/:course_id/classes/:id - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  {
    "title": "title_class",
    "class_id":"class_id",
    "created_at":"created_date",
    "usersList":[]
  }
}
```

<h2 align ='center'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "Error": "Invalid parameters"
}
```

Deve ser enviado na url um id válido

` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "Error": "Invalid token"
}
```

Para fazer essa requisição é necessário ser admin ou ser professor nessa classe

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Error": "Classe is not found"
}
```

Deve ser passado uma classe que existe

<h2 align ='center'> Editar classe </h2>
Apenas admin e professores podem listar uma classe.

`PATCH /courses/:course_id/classes/:id`

<h2 align ='center'> Requisição </h2>

```json
{
  {
	"title": "title_class",
  }
}
```

`FORMATO DA RESPOSTA - STATUS 200`

```json
{
  {
    "title": "title_class",
    "class_id":"class_id",
    "created_at":"created_date"
  }
}
```

<h2 align ='center'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "Error": "Invalid parameters"
}
```

Deve ser enviado no corpo da requisição um nome válido

` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "Error": "Invalid token"
}
```

Para fazer essa requisição é necessário ser admin

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Error": "Classe is not found"
}
```

Deve ser passado uma classe que existe

<h2 align ='center'> Deletar uma classe </h2>
Apenas admin pode deletar uma classe.

`DELETE /courses/:course_id/classes/:id - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "message": "Deleted class successfully"
}
```

<h2 align ='center'> Possíveis erros </h2>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "Error": "Invalid parameters"
}
```

Deve ser enviado na url um id válido

` FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "Error": "Invalid token"
}
```

Para fazer essa requisição é necessário ser admin

` FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Error": "Classe is not found"
}
```

Deve ser passado uma classe que existe

<br />
<br />
<br />
<br />
---
Desenvolvido por:

```json
{
  "Daniel Leira": "Product Owner",
  "Eliane Discacciati": "Developer",
  "Henrique Schardosim": "Developer",
  "Lucas Corrêa": "Developer",
  "Paulo Vitor": "Scrum Master",
  "Raniery Almeida": "Tech Lead"
}
```
