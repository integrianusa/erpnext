from __future__ import unicode_literals
from frappe import _
from frappe.desk.moduleview import add_setup_section

def get_data():
	data = [
		{
			"label": _("Email"),
			"icon": "fa fa-envelope",
			"items": [
				{
					"type": "doctype",
					"name": "Email Digest",
					"description": _("Create and manage daily, weekly and monthly email digests.")
				},
			]
		},
		{
			"label": _("Notifications"),
			"icon": "fa fa-envelope",
			"items": [
				{
					"type": "doctype",
					"name": "SMS Settings",
					"description": _("Setup SMS gateway settings")
				},
			]
		},
		{
			"label": _("Printing"),
			"icon": "fa fa-print",
			"items": [
				{
					"type": "doctype",
					"name": "Print Heading",
					"description": _("Titles for print templates e.g. Proforma Invoice.")
				},
				{
					"type": "doctype",
					"name": "Letter Head",
					"description": _("Letter Heads for print templates."),
					"onboard": 1,
				},
			]
		},
	]

	for module, label, icon in (
		("accounts", _("Accounting"), "fa fa-money"),
		("stock", _("Stock"), "fa fa-truck"),
		("selling", _("Selling"), "fa fa-tag"),
		("buying", _("Buying"), "fa fa-shopping-cart"),
		("hr", _("Human Resources"), "fa fa-group"),
		("support", _("Support"), "fa fa-phone")):

		add_setup_section(data, "erpnext", module, label, icon)

	return data
