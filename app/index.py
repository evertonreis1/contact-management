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
        Esta função adiciona um novo contato à lista de contatos.
        A lista é ordenada por sobrenome e depois por nome.
        """
        new_contact = Contact(primeiro_nome, ultimo_nome, numero_telefone)
        if self.head is None:  # se a lista está vazia
            self.head = new_contact
            self.tail = new_contact
        else:
            current_node = self.head
            while current_node is not None and (current_node.ultimo_nome + current_node.primeiro_nome) < (ultimo_nome + primeiro_nome):
                # percorre a lista até encontrar o local onde o novo contato deve ser adicionado
                current_node = current_node.next
            if current_node is None:  # adiciona o novo contato ao final da lista
                self.tail.next = new_contact
                new_contact.prev = self.tail
                self.tail = new_contact
            elif current_node.prev is None:  # adiciona o novo contato ao início da lista
                new_contact.next = self.head
                self.head.prev = new_contact
                self.head = new_contact
            else:  # adiciona o novo contato no meio da lista
                new_contact.prev = current_node.prev
                current_node.prev.next = new_contact
                new_contact.next = current_node
                current_node.prev = new_contact

    def find_contact_by_name(self, name):
        """
        Esta função utiliza busca binária para encontrar um contato pelo nome completo.
        """
        first = 0
        last = self.get_length() - 1
        while first <= last:
            middle = (first + last) // 2
            current_node = self.get_node_at_index(middle)
            full_name = current_node.ultimo_nome + current_node.primeiro_nome
            if full_name == name:
                return current_node
            elif full_name < name:
                first = middle + 1
            else:
                last = middle - 1
        return None

    def get_length(self):
        """
        Esta função retorna o tamanho da lista de contatos.
        """
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    def get_node_at_index(self,index):
        """
        Esta função retorna o contato no índice dado.
        """
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index < index:
            current_index += 1
            current_node = current_node.next
        return current_node




contact_list = ContactList()

contact_list.add_contact("Reis", "Everton", "82996246708")
contact_list.add_contact("Reis", "Evelyn", "82928392831")
contact_list.add_contact("Brown", "Charlie", "345-678-9012")

contact = contact_list.find_contact_by_name("EvelynReis")  # usando nome completo
if contact is not None:
    print(contact.numero_telefone)
else:
    print("Contato não encontrado.")

contact = contact_list.find_contact_by_name("EvertonReis")  # usando nome completo
if contact is not None:
    print(contact.numero_telefone)
else:
    print("Contato não encontrado.")
