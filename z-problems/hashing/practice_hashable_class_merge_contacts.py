from typing import *

class ContactList:
    def __init__(self, names):
        self.names = names

    def __hash__(self):
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(other.names)

    
def merge_contact_lists(contacts: List[ContactList]) -> ContactList:
    return list(set(contacts))