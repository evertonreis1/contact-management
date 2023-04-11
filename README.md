## 🧾 Contact management

Esse código implementa uma lista de contatos que permite adicionar, remover, pesquisar e listar contatos. Ele usa uma classe Contact para representar um contato e uma classe ContactList para gerenciar a lista de contatos. A lista de contatos é implementada como uma lista duplamente encadeada, o que permite adicionar contatos em ordem alfabética. O programa oferece um menu de opções para o usuário selecionar e executar as ações desejadas.

*O método **add_contact** da classe ContactList adiciona um novo contato à lista de contatos em ordem alfabética, percorrendo a lista até encontrar o local correto para inserir o novo contato.*

*O método **find_contact_by_name** da classe ContactList pesquisa um contato pelo seu nome completo utilizando uma busca binária, que é uma técnica de busca eficiente em listas ordenadas.*

*O método **get_length** da classe ContactList retorna o número de contatos na lista percorrendo a lista encadeada.*

*O método **get_node_at_index** da classe ContactList retorna o contato na posição especificada na lista encadeada.*

*O método **remove_contact** da classe ContactList remove um contato da lista de contatos, ajustando as referências para manter a lista encadeada após a remoção.*

*O método **list_contacts** da classe ContactList lista todos os contatos na lista encadeada.*

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

`$ docker build -t evertonreis1/contact-management:v6.0 .`

having created the images, run the servers using:

`$ docker run -it evertonreis1/contact-management:v6.0`

https://hub.docker.com/repository/docker/evertonreis1/contact-management/general

### Technologies

---

- Python
- Docker
