## 🧾 Contact management

Este código é uma implementação de uma lista encadeada duplamente ligada que representa uma lista de contatos telefônicos. A classe Contact representa um contato individual e armazena o primeiro nome, o último nome e o número de telefone do contato, juntamente com ponteiros para o contato anterior e o próximo na lista.

A classe ContactList representa a lista de contatos e possui métodos para adicionar contatos à lista, buscar contatos por nome e obter o tamanho da lista. A função add_contact adiciona um novo contato à lista e ordena a lista por sobrenome e, em seguida, por nome. A função find_contact_by_name utiliza a busca binária para encontrar um contato pelo nome completo. A função get_length retorna o tamanho da lista de contatos e a função get_node_at_index retorna o contato no índice dado.

Implementado também um menu para gerenciar uma lista de contatos. O usuário pode escolher entre adicionar um novo contato, obter o tamanho atual da lista de contatos, procurar um contato pelo nome e sair do programa. A lista de contatos é armazenada em uma estrutura de dados de lista duplamente encadeada ordenada por sobrenome e depois por nome. O código utiliza as classes Contact e ContactList para representar cada contato e a lista de contatos, respectivamente, e as funções add_contact(), find_contact_by_name(), get_length() e get_node_at_index() para adicionar um novo contato, procurar um contato pelo nome, obter o tamanho da lista e obter um nó em um índice específico da lista:
```
Contact List Menu:
1. Add a contact
2. Get the length of the contact list
3. Find a contact by name
4. List all contacts
5. Remove a contact
6. Exit
```



## How to make it work? 🧑🏼‍💻

The project is encapsulated in docker containers. To run locally, one just needs to clone this repository:

`$ git clone https://github.com/evertonreis/contact-management`

and build the images using:

`$ docker build -t evertonreis1/contact-management:v5.0 .`

having created the images, run the servers using:

`$ docker run -it evertonreis1/contact-management:v5.0`

https://hub.docker.com/repository/docker/evertonreis1/contact-management/general

### Technologies

---

- Python
- Docker
