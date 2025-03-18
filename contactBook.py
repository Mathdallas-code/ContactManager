from contact import Contact as cnt
import os
import json

with open("contacts.json", "r") as f:
    contactsJson = json.load(f)


class ContactBook:
    def __init__(self):
        self.contacts = contactsJson

    def addContact(self, contact: cnt):
        self.contacts[contact.id] = {
            "name": contact.name,
            "contact": contact.contact,
            "email": contact.email,
        }

        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f)
            f.close()

    def deleteContact(self, id: str):
        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f)
            f.close()
        del self.contacts[id]
        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f)
            f.close()

    def viewContacts(self):
        f = open("contacts.json", "r")
        entries = json.load(f)
        return entries
