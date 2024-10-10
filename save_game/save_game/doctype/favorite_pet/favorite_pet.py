# Copyright (c) 2024, roman.zyryanov and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FavoritePet(Document):
    def before_insert(self):
       
        existing_docs = frappe.get_all(
            "Favorite Pet",
            filters={"owner": frappe.session.user},
            fields=["name"]
        )
        
        if self.pet in ['DINOSAUR', 'Dragon']:
            frappe.throw('Мы не в попаданческом романе!')

        if existing_docs:
            for doc in existing_docs:
                frappe.delete_doc("Favorite Pet", doc.name, force=True)

        frappe.msgprint(f'{self.pet} person, I see now!')
        