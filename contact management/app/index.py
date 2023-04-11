class Contact:
    def __init__(self, primeiro_nome, ultimo_nome, numero_telefone):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.numero_telefone = numero_telefone
        self.prev = None  
        self.next = None  

class ContactList:
    def __init__(self):
        self.head = None  
        self.tail = None  

    def add_contact(self, primeiro_nome, ultimo_nome, numero_telefone):
        new_contact = Contact(primeiro_nome, ultimo_nome, numero_telefone)
        if self.head is None:  
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

        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    def get_node_at_index(self,index):
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index < index:
            current_index += 1
            current_node = current_node.next
        return current_node
    

    def remove_contact(self, contact):
        if contact is None:
            return
        if contact.prev is None and contact.next is None: 
            self.head = None
            self.tail = None
        elif contact.prev is None: 
            self.head = contact.next
            self.head.prev = None
        elif contact.next is None: 
            self.tail = contact.prev
            self.tail.next=None
        else: 
            contact.prev.next = contact.next
            contact.next.prev = contact.prev

    def list_contacts(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.primeiro_nome, current_node.ultimo_nome, current_node.numero_telefone)
            current_node = current_node.next




#
import os #estava dando erro no modo interativo "EOFError: EOF when reading a line", entao foi necessário usando os

def main():
    contact_list = ContactList()
    while True:
        print("Contact List Menu:")
        print("1. Add a contact")
        print("2. Get the length of the contact list")
        print("3. Find a contact by name")
        print("4. List all contacts")
        print("5. Remove a contact")
        print("6. Exit")

        while True:

                choice = input("Enter your choice: ")
                if choice.strip(): 
                    break
                else:
                    choice = input()
                break

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            contact_list.add_contact(first_name, last_name, phone_number)
        elif choice == "2":
            print("The contact list has", contact_list.get_length(), "contacts")
        elif choice == "3":
            name = input("Enter full name: ")
            contact = contact_list.find_contact_by_name(name)
            if contact is None:
                print("Contact not found")
            else:
                print(contact.primeiro_nome, contact.ultimo_nome, contact.numero_telefone)
        elif choice == "4":
            contact_list.list_contacts()
        elif choice == "5":
            name = input("Enter full name of the contact you want to remove: ")
            contact = contact_list.find_contact_by_name(name)
            contact_list.remove_contact(contact)

        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()




