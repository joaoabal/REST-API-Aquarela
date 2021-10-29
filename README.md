# Desafio Back-End

## API

<p align="left">API com o propósito de gerenciamento de colaboradores de uma
empresa fictícia. A API é integrada com um banco de dados PostgreSQL e é capaz de inserir, buscar, 
alterar e deletar usuários no banco.</p>

<h4 align="center"> 
Estado do Projeto: concluído 🚀
</h4>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre](#sobre)
      * [Funções](#funcoes)
      * [Atributos](#atributos)
      * [Mais](#mais)
   * [Pre Requisitos](#pre-requisitos)
   * [Rodando o Back-End](#remote-files)
   * [Tecnologias](#tecnologias)
   * [Autor](#autor)
<!--te-->

### Sobre

A API foi desenvolvida especialmente para o desafio Back-End Aquarela Advanced Analytics. 

#### Funções

A API utiliza do número de matrícula como chave primária e exclusiva de cada colaborador. Através dela, pode-se realizar as seguintes tarefas:

- [x] Cadastro de usuário
- [x] Busca por usuário
- [x] Atualização das informações do usuário
- [x] Deleção do usuário

Cada colaborador pode conter as seguintes informações além da própria matrícula:
Nome, Sobrenome, Cargo, Código do Cargo, Líder, Matrícula do Líder, Salaŕio, Senha, Status do Colaborador.

#### Atributos

- [x] Open API (Swagger)
- [x] Linguagem Python
- [x] Flask/Flask-restful
- [x] PostgreeSQL
- [x] Clean Code
- [x] Documentação do código (Docstring) e README
- [x] Git
- [x] TDD

##### Mais

A documentação foi redigida em português uma vez que a empresa fictícia utiliza chaves em português.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Swagger Viewer](https://marketplace.visualstudio.com/items?itemName=Arjun.swagger-viewer), para teste da API;
- [PostgreSQL 14](https://www.postgresql.org/); 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

As versões das bibliotecas utilizadas foram as seguintes:
- flask=="1.1.2"
- flask_restful
- flask_cors=="3.0.10"
- flask_sqlalchemy=="2.5.1"
- unittest
- psycopg2=="2.9.1"
- Python=="3.8.11"

### 🎲 Rodando o Back-End (servidor)

```bash
# Clone este repositório
$ git clone <https://github.com/tgmarinho/nlw1>

# Acesse a pasta do projeto no terminal/cmd
$ cd API-AQUARELA

# Vá para a pasta server
$ cd server

# Instale as dependências
$ npm install

# Execute a aplicação em modo de desenvolvimento
$ npm run dev:server

# O servidor inciará na porta:3333 - acesse <http://localhost:3333>
```

### Tecnologias

As seguintes ferramentas foram utilizadas na construção do projeto:

- [VisualStudio](https://visualstudio.microsoft.com/pt-br/)
- [Swagger Viewer](https://marketplace.visualstudio.com/items?itemName=Arjun.swagger-viewer)
- [Postman](https://www.postman.com/)
- [PostgreSQL 14](https://www.postgresql.org/)

### Autor

João Pedro Kleinbung Abal
Engenheiro físico e Mestre em Física pela Universidade Federal do Rio Grande do Sul (UFRGS).