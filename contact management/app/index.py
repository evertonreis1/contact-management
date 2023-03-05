class Contact:
    def __init__(self, primeiro_nome, ultimo_nome, numero_telefone):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.numero_telefone = numero_telefone
        self.prev = None  # ponteiro para o contato anterior na lista
        self.next = None  # ponteiro para o próximo contato na lista

class ContactList:
    def __init__(self):
        self.head = None  # ponteiro para o primeiro contato na lista
        self.tail = None  # ponteiro para o último contato na lista

    def add_contact(self, primeiro_nome, ultimo_nome, numero_telefone):
        """
        Esta função adiciona um novo contato a lista de contatos.
        A lista é ordenada por sobrenome e depois por nome.
        """
        novo_contato = Contact(primeiro_nome, ultimo_nome, numero_telefone)
        if self.head is None:  # se a lista está vazia
            self.head = novo_contato
            self.tail = novo_contato
        else:
            current_node = self.head
            while current_node is not None and (current_node.ultimo_nome + current_node.primeiro_nome) < (ultimo_nome + primeiro_nome):
                # percorre a lista até encontrar o local onde o novo contato deve ser adicionado
                current_node = current_node.next
            if current_node is None:  # adiciona o novo contato ao final da lista
                self.tail.next = novo_contato
                novo_contato.prev = self.tail
                self.tail = novo_contato
            elif current_node.prev is None:  # adiciona o novo contato ao início da lista
                novo_contato.next = self.head
                self.head.prev = novo_contato
                self.head = novo_contato
            else:  # adiciona o novo contato no meio da lista
                novo_contato.prev = current_node.prev
                current_node.prev.next = novo_contato
                novo_contato.next = current_node
                current_node.prev = novo_contato


minha_lista_de_contatos = ContactList()


minha_lista_de_contatos.add_contact("Julia", "Clara", "829234-5678")
minha_lista_de_contatos.add_contact("Everton", "Reis", "829345-6789")
minha_lista_de_contatos.add_contact("Pedro", "Raul", "829456-7890")
minha_lista_de_contatos.add_contact("Ana", "Banana", "829567-8901")

contato_atual = minha_lista_de_contatos.head
while contato_atual is not None:
    print(f"{contato_atual.primeiro_nome} {contato_atual.ultimo_nome}: {contato_atual.numero_telefone}")
    contato_atual = contato_atual.next
