## 🧾 Contact management

Este código é uma implementação de uma lista encadeada duplamente ligada que representa uma lista de contatos telefônicos. A classe Contact representa um contato individual e armazena o primeiro nome, o último nome e o número de telefone do contato, juntamente com ponteiros para o contato anterior e o próximo na lista.

A classe ContactList representa a lista de contatos e possui métodos para adicionar contatos à lista, buscar contatos por nome e obter o tamanho da lista. A função add_contact adiciona um novo contato à lista e ordena a lista por sobrenome e, em seguida, por nome. A função find_contact_by_name utiliza a busca binária para encontrar um contato pelo nome completo. A função get_length retorna o tamanho da lista de contatos e a função get_node_at_index retorna o contato no índice dado.

Nessa instância, é criada uma lista de contatos vazia, em seguida, três contatos são adicionados à lista usando o método add_contact. Em seguida, são realizadas duas buscas na lista de contatos: a primeira usando o método find_contact_by_name para encontrar o telefone de "Everton Reis" e a segunda usando o método get_node_at_index para encontrar o contato no índice 1. O resultado das buscas é impresso na tela. O resultado final é:
```
Tamanho da lista de contatos: 3
Contato não encontrado.
Telefone do contato no índice 1 : 8288834388
```



## How to make it work? 🧑🏼‍💻

The project is encapsulated in docker containers. To run locally, one just needs to clone this repository:

`$ git clone https://github.com/evertonreis/contact-management`

and build the images using:

`$ docker build -t evertonreis1/contact-management:v2.0 .`

having created the images, run the servers using:

`$ docker run -it evertonreis1/contact-management`

https://hub.docker.com/repository/docker/evertonreis1/contact-management/general

### Technologies

---

- Python
- Docker
