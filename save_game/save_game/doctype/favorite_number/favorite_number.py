# Copyright (c) 2024, roman.zyryanov and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FavoriteNumber(Document):
    def before_insert(self):
        if self.number > 1000:
            frappe.throw("Слишком большое число!")
        
        existing_docs = frappe.get_all(
            "Favorite Number",
            filters={"owner": frappe.session.user},
            fields=["name"]
        )

        if existing_docs:
            for doc in existing_docs:
                frappe.delete_doc("Favorite Number", doc.name, force=True)

        if self.number in [666, 13]:
            frappe.msgprint("Здравствуйте, Владыка")
        else:
            frappe.msgprint(f"Ваше новое любимое число - {self.number}")


