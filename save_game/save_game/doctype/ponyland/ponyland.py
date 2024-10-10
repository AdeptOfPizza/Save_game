# Copyright (c) 2024, roman.zyryanov and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Ponyland(Document):
	def before_insert(self):
       
		existing_docs = frappe.get_all(
			"Ponyland",
			filters={"owner": frappe.session.user},
			fields=["name"]
		)
        
		if existing_docs:
			for doc in existing_docs:
				frappe.delete_doc("Ponyland", doc.name, force=True)

#	def before_save(self):
#		favorite_pet = frappe.get_doc("Favorite Pet", {"owner": frappe.session.user})
#
#		if self.are_you_a_pony_person == 'No':
#			frappe.throw("""Verily, honesty is a virtue, dear friend. 
#							Yet, so long as thou dost not cherish such graceful and magical creatures, 
#							the gates of Ponyland shall be forever closed to thee!""")
		
#		elif favorite_pet.pet != 'Pony':
#			frappe.throw("""Thou art a liar and a scoundrel! 
#				How dost thou dare speak such brazen falsehood? 
#				Only recently, sir, didst thou claim that ponies 
#				were not thy favorite creatures. 
#				Shame upon thee for uttering such a woeful untruth!""")
			
#		else:
#			frappe.msgprint("""What joy! Verily, verily, I see at once 
#				   a true connoisseur of the sublime! 
#				   Come forth, then, to Ponyland, where I shall 
#				   introduce thee to these magnificent creatures! 
##				   Let us tarry not a moment longer!""")
			
	def before_save(self):
		favorite_pet = frappe.get_all("Favorite Pet", filters={"owner": frappe.session.user}, fields=["pet"])

		if not favorite_pet:
			frappe.throw("""
                Thou hast not yet chosen thy beloved pet. 
                Return to the gates of Ponyland when thou art ready 
                to make thy choice.
            """)
        
		if self.are_you_a_pony_person == 'No':
			frappe.throw("""
                Verily, honesty is a virtue, dear friend. 
                Yet, so long as thou dost not cherish such graceful 
                and magical creatures, the gates of Ponyland 
                shall be forever closed to thee!
            """)

		if favorite_pet[0].pet != 'Pony':
			frappe.throw("""
                Thou art a liar and a scoundrel! 
                How dost thou dare speak such brazen falsehood? 
                Only recently, sir, didst thou claim that ponies 
                were not thy favorite creatures. 
                Shame upon thee for uttering such a woeful untruth!
            """)

		frappe.msgprint("""
            What joy! Verily, verily, I see at once a true connoisseur 
            of the sublime! Come forth, then, to Ponyland, where I shall 
            introduce thee to these magnificent creatures! 
            Let us tarry not a moment longer!
        """)

