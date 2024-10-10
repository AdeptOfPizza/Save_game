# Copyright (c) 2024, roman.zyryanov and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class HotPotato(Document):
	def before_insert(self):
       
		existing_docs = frappe.get_all(
			"Hot Potato",
			filters={"owner": frappe.session.user},
			fields=["name"]
		)

		if existing_docs:
			for doc in existing_docs:
				frappe.delete_doc("Hot Potato", doc.name, force=True)
  

	def before_save(self):
		if self.number > 1000:
			frappe.throw('Ну куда так много?')

		key_doc = frappe.get_single('Save Key')   
		the_key = key_doc.key                    
		difference = abs(self.number - the_key)
		Hints = {
		500:"Антарктида",
		350:"Очень Холодно",
		250:"Холодно",
		150:"Прохладно",
		100:"Чуть прохладно",
		50:"Тепло",
		35:"Очень тепло",
		25:"Горячо",
		15:"Очень горячо!",
		10:"Огонь!",
		7:"Раскаленная печь!",
		4:"Извержение вулкана!",
		2:"ПОВЕРХНОСТЬ СОЛНЦА!!",
		0:"Температура Планка (Выше некуда)",
		}

		for threshhold, message in Hints.items():
			if difference > threshhold:
				frappe.throw(message)

#      меняем константу на следующую попытку
		key_doc.key = random.randint(1,1000)
		key_doc.save()

