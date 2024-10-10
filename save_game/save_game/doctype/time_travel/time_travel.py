# Copyright (c) 2024, roman.zyryanov and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate
from frappe.utils import getdate


class TimeTravel(Document):
	def before_insert(self):
       
		existing_docs = frappe.get_all(
			"Time Travel",
			filters={"owner": frappe.session.user},
			fields=["name"]
		)
        
		if existing_docs:
			for doc in existing_docs:
				frappe.delete_doc("Time Travel", doc.name, force=True)
	
	def before_save(self):
		today = getdate(nowdate())
		birthdate = getdate(self.your_date_of_birth)
		if today > birthdate:
			frappe.throw('You are not from the future!')

		else:
			frappe.msgprint('...а для завтра что сегодня сделал я?...')