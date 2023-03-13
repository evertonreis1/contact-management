## 🧾 Contact management

Este código é uma implementação de uma lista encadeada duplamente ligada que representa uma lista de contatos telefônicos. A classe Contact representa um contato individual e armazena o primeiro nome, o último nome e o número de telefone do contato, juntamente com ponteiros para o contato anterior e o próximo na lista.

A classe ContactList representa a lista de contatos e possui métodos para adicionar contatos à lista, buscar contatos por nome e obter o tamanho da lista. A função add_contact adiciona um novo contato à lista e ordena a lista por sobrenome e, em seguida, por nome. A função find_contact_by_name utiliza a busca binária para encontrar um contato pelo nome completo. A função get_length retorna o tamanho da lista de contatos e a função get_node_at_index retorna o contato no índice dado.

O código adiciona alguns contatos de exemplo à lista e depois procura contatos pelo nome completo. Se o contato for encontrado, o número de telefone é impresso, caso contrário, uma mensagem de "Contato não encontrado" é exibida.



## How to make it work? 🧑🏼‍💻

The project is encapsulated in docker containers. To run locally, one just needs to clone this repository:

`$ git clone https://github.com/evertonreis/contact-management`

and build the images using:

`$ docker build -t evertonreis1/contact-management:latest .`

having created the images, run the servers using:

`$ docker run -it evertonreis1/contact-management`



### Technologies

---

- Python
