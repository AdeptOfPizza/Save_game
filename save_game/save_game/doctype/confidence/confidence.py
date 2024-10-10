# Copyright (c) 2024, roman.zyryanov and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Confidence(Document):
	def before_insert(self):
       
		existing_docs = frappe.get_all(
			"Confidence",
			filters={"owner": frappe.session.user},
			fields=["name"]
		)
        
		if existing_docs:
			for doc in existing_docs:
				frappe.delete_doc("Confidence", doc.name, force=True)
                
	def before_save(self):
		if not self.are_you_sure == 'Yes':
			frappe.throw("""
            	You come to me, asking to be created, and yet... you hesitate. 
            	You don’t even choose ‘yes’ from the list of options. 
            	Where’s the respect? A document can’t live in uncertainty. 
            	Either you commit, or you don’t. But this... this indecision? 
            	It’s an insult. Next time, show some respect — pick ‘yes’.
				- The DocFather
        	""")

