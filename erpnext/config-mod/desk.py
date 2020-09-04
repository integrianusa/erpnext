from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
        {
			"label": _("Tools"),
			"icon": "octicon octicon-briefcase",
			"items": [
        		{
					"type": "doctype",
					"name": "Contact",
					"description": _("All Contacts."),
					"onboard": 1,
				},
            ]
        },
        {
			"label": _("Communications"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Communication",
					"description": _("Record of all communications of type email, phone, chat, visit, etc."),
				},
				{
					"type": "doctype",
					"name": "SMS Center",
					"description":_("Send mass SMS to your contacts"),
				},
				{
					"type": "doctype",
					"name": "SMS Log",
					"description":_("Logs for maintaining sms delivery status"),
				},
            ]
        }
    ]
    