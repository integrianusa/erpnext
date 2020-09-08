# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe, os, json

from frappe import _
from frappe.desk.page.setup_wizard.setup_wizard import make_records
from frappe.utils import cstr, getdate
from erpnext.accounts.doctype.account.account import RootNotEditable
from frappe.desk.doctype.global_search_settings.global_search_settings import update_global_search_doctypes

default_lead_sources = ["Existing Customer", "Reference", "Advertisement",
	"Cold Calling", "Exhibition", "Supplier Reference", "Mass Mailing",
	"Customer's Vendor", "Campaign", "Walk In"]

default_sales_partner_type = ["Channel Partner", "Distributor", "Dealer", "Agent",
	"Retailer", "Implementation Partner", "Reseller"]

#setup_wizard #1
def install(country=None):
	records = [
	# domains
		{ 'doctype': 'Domain', 'domain': 'Distribution'},
		{ 'doctype': 'Domain', 'domain': 'Manufacturing'},
		{ 'doctype': 'Domain', 'domain': 'Retail'},
		{ 'doctype': 'Domain', 'domain': 'Services'},
		{ 'doctype': 'Domain', 'domain': 'Education'},
		{ 'doctype': 'Domain', 'domain': 'Healthcare'},
		{ 'doctype': 'Domain', 'domain': 'Agriculture'},
		{ 'doctype': 'Domain', 'domain': 'Non Profit'},

	# address template
		{'doctype':"Address Template", "country": country},

	# Designation
		{'doctype': 'Designation', 'designation_name': _('CEO')},
		{'doctype': 'Designation', 'designation_name': _('Manager')},
		{'doctype': 'Designation', 'designation_name': _('Engineer')},
		{'doctype': 'Designation', 'designation_name': _('Accountant')},
		{'doctype': 'Designation', 'designation_name': _('Secretary')},
		{'doctype': 'Designation', 'designation_name': _('Associate')},
		{'doctype': 'Designation', 'designation_name': _('Finance Manager')},
		{'doctype': 'Designation', 'designation_name': _('HR Manager')},
		{'doctype': 'Designation', 'designation_name': _('Project Manager')},
		{'doctype': 'Designation', 'designation_name': _('Marketing and Sales Manager')},
		{'doctype': 'Designation', 'designation_name': _('Operation Manager')},
		{'doctype': 'Designation', 'designation_name': _('Warehouse Manager')},
		{'doctype': 'Designation', 'designation_name': _('Administrative Staff')},
		{'doctype': 'Designation', 'designation_name': _('Finance Staff')},
		{'doctype': 'Designation', 'designation_name': _('HR Staff')},
		{'doctype': 'Designation', 'designation_name': _('Marketing & Sales Staff')},

	# territory: with two default territories, one for home country and one named Rest of the World
		{'doctype': 'Territory', 'territory_name': _('All Territories'), 'is_group': 1, 'name': _('All Territories'), 'parent_territory': ''},
		{'doctype': 'Territory', 'territory_name': "Indonesia", 'is_group': 1, 'parent_territory': _('All Territories')},
		{'doctype': 'Territory', 'territory_name': _("Rest Of The World"), 'is_group': 0, 'parent_territory': _('All Territories')},
		{'doctype': 'Territory', 'territory_name': 'Nanggroe Aceh Darussalam', 'is_group': 0, 'name': 'Nanggroe Aceh Darussalam', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Sumatera Utara', 'is_group': 0, 'name': 'Sumatera Utara', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Sumatera Barat', 'is_group': 0, 'name': 'Sumatera Barat', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Riau', 'is_group': 0, 'name': 'Riau', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Kepulauan Riau', 'is_group': 0, 'name': 'Kepulauan Riau', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Jambi', 'is_group': 0, 'name': 'Jambi', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Sumatera Selatan', 'is_group': 0, 'name': 'Sumatera Selatan', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Bangka Belitung', 'is_group': 0, 'name': 'Bangka Belitung', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Bengkulu', 'is_group': 0, 'name': 'Bengkulu', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Lampung', 'is_group': 0, 'name': 'Lampung', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'DKI Jakarta', 'is_group': 0, 'name': 'DKI Jakarta', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Jawa Barat', 'is_group': 0, 'name': 'Jawa Barat', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Banten', 'is_group': 0, 'name': 'Banten', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Jawa Tengah', 'is_group': 0, 'name': 'Jawa Tengah', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'DI Yogyakarta', 'is_group': 0, 'name': 'DI Yogyakarta', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Jawa Timur', 'is_group': 0, 'name': 'Jawa Timur', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Bali', 'is_group': 0, 'name': 'Bali', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Nusa Tenggara Barat', 'is_group': 0, 'name': 'Nusa Tenggara Barat', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Nusa Tenggara Timur', 'is_group': 0, 'name': 'Nusa Tenggara Timur', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Kalimantan Barat', 'is_group': 0, 'name': 'Kalimantan Barat', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Kalimantan Tengah', 'is_group': 0, 'name': 'Kalimantan Tengah', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Kalimantan Selatan', 'is_group': 0, 'name': 'Kalimantan Selatan', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Kalimantan Timur', 'is_group': 0, 'name': 'Kalimantan Timur', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Kalimantan Utara', 'is_group': 0, 'name': 'Kalimantan Utara', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Sulawesi Utara', 'is_group': 0, 'name': 'Sulawesi Utara', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Sulawesi Barat', 'is_group': 0, 'name': 'Sulawesi Barat', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Sulawesi Tengah', 'is_group': 0, 'name': 'Sulawesi Tengah', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Sulawesi Tenggara', 'is_group': 0, 'name': 'Sulawesi Tenggara', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Sulawesi Selatan', 'is_group': 0, 'name': 'Sulawesi Selatan', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Gorontalo', 'is_group': 0, 'name': 'Gorontalo', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Maluku', 'is_group': 0, 'name': 'Maluku', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Maluku Utara', 'is_group': 0, 'name': 'Maluku Utara', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Papua Barat', 'is_group': 0, 'name': 'Papua Barat', 'parent_territory': 'Indonesia'},
		{'doctype': 'Territory', 'territory_name': 'Papua', 'is_group': 0, 'name': 'Papua', 'parent_territory': 'Indonesia'},

	# item group
		{'doctype': 'Item Group', 'item_group_name': _('All Item Groups'),
			'is_group': 1, 'parent_item_group': ''},
		{'doctype': 'Item Group', 'item_group_name': _('Products'),
			'is_group': 0, 'parent_item_group': _('All Item Groups'), "show_in_website": 1 },
		{'doctype': 'Item Group', 'item_group_name': _('Raw Material'),
			'is_group': 0, 'parent_item_group': _('All Item Groups') },
		{'doctype': 'Item Group', 'item_group_name': _('Services'),
			'is_group': 0, 'parent_item_group': _('All Item Groups') },
		{'doctype': 'Item Group', 'item_group_name': _('Sub Assemblies'),
			'is_group': 0, 'parent_item_group': _('All Item Groups') },
		{'doctype': 'Item Group', 'item_group_name': _('Consumable'),
			'is_group': 0, 'parent_item_group': _('All Item Groups') },

	# customer group
		{'doctype': 'Customer Group', 'customer_group_name': _('All Customer Groups'), 'is_group': 1, 	'name': _('All Customer Groups'), 'parent_customer_group': ''},
		{'doctype': 'Customer Group', 'customer_group_name': _('Individual'), 'is_group': 0, 'parent_customer_group': _('All Customer Groups')},
		{'doctype': 'Customer Group', 'customer_group_name': _('Commercial'), 'is_group': 0, 'parent_customer_group': _('All Customer Groups')},
		{'doctype': 'Customer Group', 'customer_group_name': _('Non Profit'), 'is_group': 0, 'parent_customer_group': _('All Customer Groups')},
		{'doctype': 'Customer Group', 'customer_group_name': _('Government'), 'is_group': 0, 'parent_customer_group': _('All Customer Groups')},

	# supplier group
		{'doctype': 'Supplier Group', 'supplier_group_name': _('All Supplier Groups'), 'is_group': 1, 'name': _('All Supplier Groups'), 'parent_supplier_group': ''},
		{'doctype': 'Supplier Group', 'supplier_group_name': _('Services'), 'is_group': 0, 'parent_supplier_group': _('All Supplier Groups')},
		{'doctype': 'Supplier Group', 'supplier_group_name': _('Local'), 'is_group': 0, 'parent_supplier_group': _('All Supplier Groups')},
		{'doctype': 'Supplier Group', 'supplier_group_name': _('Raw Material'), 'is_group': 0, 'parent_supplier_group': _('All Supplier Groups')},
		{'doctype': 'Supplier Group', 'supplier_group_name': _('Electrical'), 'is_group': 0, 'parent_supplier_group': _('All Supplier Groups')},
		{'doctype': 'Supplier Group', 'supplier_group_name': _('Hardware'), 'is_group': 0, 'parent_supplier_group': _('All Supplier Groups')},
		{'doctype': 'Supplier Group', 'supplier_group_name': _('Distributor'), 'is_group': 0, 'parent_supplier_group': _('All Supplier Groups')},

	# salary component
		{'doctype': 'Salary Component', 'salary_component': _('Income Tax'), 'description': _('Income Tax'), 'type': 'Deduction'},
		{'doctype': 'Salary Component', 'salary_component': _('Loan Payment'), 'description': _('Employee Loan Payment'), 'type': 'Deduction'},
		{'doctype': 'Salary Component', 'salary_component': _('Basic'), 'description': _('Basic'), 'type': 'Earning'},
		{'doctype': 'Salary Component', 'salary_component': _('Arrear'), 'description': _('Arrear'), 'type': 'Earning'},
		{'doctype': 'Salary Component', 'salary_component': _('Leave Encashment'), 'description': _('Leave Encashment'), 'type': 'Earning'},
		{'doctype': 'Salary Component', 'salary_component': _('Bonus'), 'description': _('Bonus Allowances'), 'type': 'Earning'},
		{'doctype': 'Salary Component', 'salary_component': _('Tunjangan Hari Raya'), 'description': _('THR'), 'type': 'Earning'},
		{'doctype': 'Salary Component', 'salary_component': _('Allowances'), 'description': _('Other allowances'), 'type': 'Earning'},

	# expense claim type
		{'doctype': 'Expense Claim Type', 'name': _('Calls'), 'expense_type': _('Calls')},
		{'doctype': 'Expense Claim Type', 'name': _('Food'), 'expense_type': _('Food')},
		{'doctype': 'Expense Claim Type', 'name': _('Medical'), 'expense_type': _('Medical')},
		{'doctype': 'Expense Claim Type', 'name': _('Travel'), 'expense_type': _('Travel')},
		{'doctype': 'Expense Claim Type', 'name': _('Accomodations'), 'expense_type': _('Accomodations')},
		{'doctype': 'Expense Claim Type', 'name': _('Others'), 'expense_type': _('Others')},

	# leave type
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Orang Serumah Meninggal'), 'name': _('Cuti Orang Serumah Meninggal'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 0,
			'is_carry_forward': 0, 'is_compensatory': 0, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 1, 'max_leaves_allowed': 1},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Keluarga Dekat Meninggal'), 'name': _('Cuti Keluarga Dekat Meninggal'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 0,
			'is_carry_forward': 0, 'is_compensatory': 0, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 2, 'max_leaves_allowed': 2},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Melahirkan/Keguguran'), 'name': _('Cuti Melahirkan/Keguguran'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 1,
			'is_carry_forward': 0, 'is_compensatory': 0, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 90, 'max_leaves_allowed': 1},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Membaptiskan Anak'), 'name': _('Cuti Membaptiskan Anak'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 0,
			'is_carry_forward': 0, 'is_compensatory': 0, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 2, 'max_leaves_allowed': 1},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Mengkhitankan Anak'), 'name': _('Cuti Mengkhitankan Anak'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 0,
			'is_carry_forward': 0, 'is_compensatory': 0, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 2, 'max_leaves_allowed': 2},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Menikahkan Anak'), 'name': _('Cuti Menikahkan Anak'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 0,
			'is_carry_forward': 0, 'is_compensatory': 0, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 0, 'max_leaves_allowed': 2},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Kompensasi Hari Libur'), 'name': _('Cuti Kompensasi Hari Libur'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 0,
			'is_carry_forward': 0, 'is_compensatory': 1, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 0, 'max_leaves_allowed': 0},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Besar'), 'name': _('Cuti Besar'), 'applicable_after': 1728,
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 1,
			'is_carry_forward': 0, 'is_compensatory': 0, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 30, 'max_leaves_allowed': 0},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Tahunan'), 'name': _('Cuti Tahunan'), 'applicable_after': 288,
			'allow_encashment': 0, 'earned_leave_frequency': 'Yearly', 'include_holiday': 0,
			'is_carry_forward': 0, 'is_compensatory': 0, 'is_earned_leave': 1, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 12, 'max_leaves_allowed': 12},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Tanpa Upah'), 'name': _('Cuti Tanpa Upah'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 1,
			'is_carry_forward': 0, 'is_compensatory': 0, 'is_earned_leave': 0, 'is_lwp': 1,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 12, 'max_leaves_allowed': 0},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Sakit'), 'name': _('Cuti Sakit'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 1,
			'is_carry_forward': 0, 'is_compensatory': 0, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 0, 'max_leaves_allowed': 0},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Bersama'), 'name': _('Cuti Bersama'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 0,
			'is_carry_forward': 0, 'is_compensatory': 1, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 0, 'max_leaves_allowed': 0},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Keluarga Dekat Rawat Inap'), 'name': _('Cuti Keluarga Dekat Rawat Inap'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 0,
			'is_carry_forward': 0, 'is_compensatory': 1, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 1, 'max_leaves_allowed': 1},
		{'doctype': 'Leave Type', 'leave_type_name': _('Cuti Istri Melahirkan/Keguguran'), 'name': _('Cuti Istri Melahirkan/Keguguran'),
			'allow_encashment': 0, 'earned_leave_frequency': 'Monthly', 'include_holiday': 0,
			'is_carry_forward': 0, 'is_compensatory': 1, 'is_earned_leave': 0, 'is_lwp': 0,
			'is_optional_leave': 0, 'max_continuous_days_allowed': 7, 'max_leaves_allowed': 1},

	# Employment Type
		{'doctype': 'Employment Type', 'employee_type_name': _('Full-time')},
		{'doctype': 'Employment Type', 'employee_type_name': _('Part-time')},
		{'doctype': 'Employment Type', 'employee_type_name': _('Probation')},
		{'doctype': 'Employment Type', 'employee_type_name': _('Contract')},
		{'doctype': 'Employment Type', 'employee_type_name': _('Commission')},
		{'doctype': 'Employment Type', 'employee_type_name': _('Piecework')},
		{'doctype': 'Employment Type', 'employee_type_name': _('Intern')},
		{'doctype': 'Employment Type', 'employee_type_name': _('Apprentice')},

	# Employee Health Insurance
		{'doctype': 'Employee Health Insurance', 'health_insurance_name': _('Asuransi non-BPJS')},
		{'doctype': 'Employee Health Insurance', 'health_insurance_name': _('BPJS Pensiun')},
		{'doctype': 'Employee Health Insurance', 'health_insurance_name': _('BPJS Kesehatan')},
		{'doctype': 'Employee Health Insurance', 'health_insurance_name': _('BPJS Tenagakerja')},

	# Stock Entry Type
		{'doctype': 'Stock Entry Type', 'name': 'Material Issue', 'purpose': 'Material Issue'},
		{'doctype': 'Stock Entry Type', 'name': 'Material Receipt', 'purpose': 'Material Receipt'},
		{'doctype': 'Stock Entry Type', 'name': 'Material Transfer', 'purpose': 'Material Transfer'},
		{'doctype': 'Stock Entry Type', 'name': 'Manufacture', 'purpose': 'Manufacture'},
		{'doctype': 'Stock Entry Type', 'name': 'Repack', 'purpose': 'Repack'},
		{'doctype': 'Stock Entry Type', 'name': 'Send to Subcontractor', 'purpose': 'Send to Subcontractor'},
		{'doctype': 'Stock Entry Type', 'name': 'Material Transfer for Manufacture', 'purpose': 'Material Transfer for Manufacture'},
		{'doctype': 'Stock Entry Type', 'name': 'Material Consumption for Manufacture', 'purpose': 'Material Consumption for Manufacture'},
		{'doctype': 'Stock Entry Type', 'name': 'Send to Warehouse', 'purpose': 'Send to Warehouse'},
		{'doctype': 'Stock Entry Type', 'name': 'Receive at Warehouse', 'purpose': 'Receive at Warehouse'},

	# Sales Person
		{'doctype': 'Sales Person', 'sales_person_name': _('Sales Team'), 'is_group': 1, "parent_sales_person": ""},

	# Mode of Payment
		{'doctype': 'Mode of Payment',
			'mode_of_payment': 'Check' if country in {"United States", "Indonesia"} else _('Cheque'),
			'type': 'Bank'},
		{'doctype': 'Mode of Payment', 'mode_of_payment': _('Cash'),
			'type': 'Cash'},
		{'doctype': 'Mode of Payment', 'mode_of_payment': _('Credit Card'),
			'type': 'Bank'},
		{'doctype': 'Mode of Payment', 'mode_of_payment': _('Debit Card'),
			'type': 'Bank'},
		{'doctype': 'Mode of Payment', 'mode_of_payment': _('Wire Transfer'),
			'type': 'Bank'},
		{'doctype': 'Mode of Payment', 'mode_of_payment': _('Bank Draft'),
			'type': 'Bank'},
		{'doctype': 'Mode of Payment', 'mode_of_payment': _('Cashless'),
			'type': 'Bank'},

	# Activity Type
		{'doctype': 'Activity Type', 'activity_type': _('Planning')},
		{'doctype': 'Activity Type', 'activity_type': _('Research')},
		{'doctype': 'Activity Type', 'activity_type': _('Proposal Writing')},
		{'doctype': 'Activity Type', 'activity_type': _('Execution')},
		{'doctype': 'Activity Type', 'activity_type': _('Communication')},

	# Item Attribute
		{'doctype': "Item Attribute", "attribute_name": _("Size"), "item_attribute_values": [
			{"attribute_value": _("Extra Small"), "abbr": "XS"},
			{"attribute_value": _("Small"), "abbr": "S"},
			{"attribute_value": _("Medium"), "abbr": "M"},
			{"attribute_value": _("Large"), "abbr": "L"},
			{"attribute_value": _("Extra Large"), "abbr": "XL"}
		]},

		{'doctype': "Item Attribute", "attribute_name": _("Colour"), "item_attribute_values": [
			{"attribute_value": _("Red"), "abbr": "RED"},
			{"attribute_value": _("Green"), "abbr": "GRE"},
			{"attribute_value": _("Blue"), "abbr": "BLU"},
			{"attribute_value": _("Black"), "abbr": "BLA"},
			{"attribute_value": _("White"), "abbr": "WHI"}
		]},

	# Issue Priority
		{'doctype': 'Issue Priority', 'name': _('Low')},
		{'doctype': 'Issue Priority', 'name': _('Medium')},
		{'doctype': 'Issue Priority', 'name': _('High')},

	# Job Applicant Source
		{'doctype': 'Job Applicant Source', 'source_name': _('Website Listing')},
		{'doctype': 'Job Applicant Source', 'source_name': _('Walk In')},
		{'doctype': 'Job Applicant Source', 'source_name': _('Employee Referral')},
		{'doctype': 'Job Applicant Source', 'source_name': _('Campaign')},

	# Party Type
		{'doctype': "Party Type", "party_type": "Customer", "account_type": "Receivable"},
		{'doctype': "Party Type", "party_type": "Supplier", "account_type": "Payable"},
		{'doctype': "Party Type", "party_type": "Employee", "account_type": "Payable"},
		{'doctype': "Party Type", "party_type": "Member", "account_type": "Receivable"},
		{'doctype': "Party Type", "party_type": "Shareholder", "account_type": "Payable"},
		{'doctype': "Party Type", "party_type": "Student", "account_type": "Receivable"},

	# Opportunity Type
		{'doctype': "Opportunity Type", "name": _("Sales")},
		{'doctype': "Opportunity Type", "name": _("Support")},
		{'doctype': "Opportunity Type", "name": _("Maintenance")},

	# Project Type
		{'doctype': "Project Type", "project_type": _("Internal")},
		{'doctype': "Project Type", "project_type": _("External")},
		{'doctype': "Project Type", "project_type": _("Other")},

	# Offer Term
		{"doctype": "Offer Term", "offer_term": _("Date of Joining")},
		{"doctype": "Offer Term", "offer_term": _("Annual Salary")},
		{"doctype": "Offer Term", "offer_term": _("Probationary Period")},
		{"doctype": "Offer Term", "offer_term": _("Employee Benefits")},
		{"doctype": "Offer Term", "offer_term": _("Working Hours")},
		{"doctype": "Offer Term", "offer_term": _("Stock Options")},
		{"doctype": "Offer Term", "offer_term": _("Department")},
		{"doctype": "Offer Term", "offer_term": _("Job Description")},
		{"doctype": "Offer Term", "offer_term": _("Responsibilities")},
		{"doctype": "Offer Term", "offer_term": _("Leaves per Year")},
		{"doctype": "Offer Term", "offer_term": _("Notice Period")},
		{"doctype": "Offer Term", "offer_term": _("Incentives")},

	# Assessment Group
		{'doctype': 'Assessment Group', 'assessment_group_name': _('All Assessment Groups'),
			'is_group': 1, 'parent_assessment_group': ''},

	# Share Management
		{"doctype": "Share Type", "title": _("Equity")},
		{"doctype": "Share Type", "title": _("Preference")},

	# Market Segments
		{"doctype": "Market Segment", "market_segment": _("Lower Income")},
		{"doctype": "Market Segment", "market_segment": _("Middle Income")},
		{"doctype": "Market Segment", "market_segment": _("Upper Income")},
		{"doctype": "Market Segment", "market_segment": _("Individuals")},
		{"doctype": "Market Segment", "market_segment": _("Commercials")},

	# Sales Stages
		{"doctype": "Sales Stage", "stage_name": _("Prospecting")},
		{"doctype": "Sales Stage", "stage_name": _("Qualification")},
		{"doctype": "Sales Stage", "stage_name": _("Needs Analysis")},
		{"doctype": "Sales Stage", "stage_name": _("Value Proposition")},
		{"doctype": "Sales Stage", "stage_name": _("Identifying Decision Makers")},
		{"doctype": "Sales Stage", "stage_name": _("Perception Analysis")},
		{"doctype": "Sales Stage", "stage_name": _("Proposal/Price Quote")},
		{"doctype": "Sales Stage", "stage_name": _("Negotiation/Review")},

	# Email Account
		{'doctype': "Email Account", "email_id": "sales@example.com", "append_to": "Opportunity"},
		{'doctype': "Email Account", "email_id": "support@example.com", "append_to": "Issue"},
		{'doctype': "Email Account", "email_id": "jobs@example.com", "append_to": "Job Applicant"},

	# Print Heading
		{'doctype': "Print Heading", 'print_heading': _("Credit Note")},
		{'doctype': "Print Heading", 'print_heading': _("Debit Note")},

	]

# industry type, lead source, sales partner type
	from erpnext.setup.setup_wizard.data.industry_type import get_industry_types
	records += [{"doctype":"Industry Type", "industry": d} for d in get_industry_types()]
	# records += [{"doctype":"Operation", "operation": d} for d in get_operations()]
	records += [{'doctype': 'Lead Source', 'source_name': _(d)} for d in default_lead_sources]

	records += [{'doctype': 'Sales Partner Type', 'sales_partner_type': _(d)} for d in default_sales_partner_type]

# hr - leave notifications
	base_path = frappe.get_app_path("erpnext", "hr", "doctype")
	response = frappe.read_file(os.path.join(base_path, "leave_application/leave_application_email_template.html"))

	records += [{'doctype': 'Email Template', 'name': _("Leave Approval Notification"), 'response': response,\
		'subject': _("Leave Approval Notification"), 'owner': frappe.session.user}]

	records += [{'doctype': 'Email Template', 'name': _("Leave Status Notification"), 'response': response,\
		'subject': _("Leave Status Notification"), 'owner': frappe.session.user}]

# stock - delivery 
	base_path = frappe.get_app_path("erpnext", "stock", "doctype")
	response = frappe.read_file(os.path.join(base_path, "delivery_trip/dispatch_notification_template.html"))

	records += [{'doctype': 'Email Template', 'name': _("Dispatch Notification"), 'response': response,\
		'subject': _("Your order is out for delivery!"), 'owner': frappe.session.user}]

# Records for the Supplier Scorecard
	from erpnext.buying.doctype.supplier_scorecard.supplier_scorecard import make_default_records
	make_default_records()
# make above record lists
	make_records(records)
# set more defaults ==>
	set_more_defaults()
# update global search ==>
	update_global_search_doctypes()

	# path = frappe.get_app_path('erpnext', 'regional', frappe.scrub(country))
	# if os.path.exists(path.encode("utf-8")):
	# 	frappe.get_attr("erpnext.regional.{0}.setup.setup_company_independent_fixtures".format(frappe.scrub(country)))()

#setup_wizard #1a
def set_more_defaults():
# Do more setup stuff that can be done here with no dependencies
# add_uom_data
	add_uom_data()
# set no copy fields of an item doctype to item variant settings
	doc = frappe.get_doc('Item Variant Settings')
	doc.set_default_fields()
	doc.save()

#setup_wizard #2
def install_company(args):
	records = [
		# Fiscal Year
		{
			'doctype': "Fiscal Year",
			'year': get_fy_details(args.fy_start_date, args.fy_end_date),
			'year_start_date': args.fy_start_date,
			'year_end_date': args.fy_end_date
		},

		# Company
		{
			"doctype":"Company",
			'company_name': args.company_name,
			'enable_perpetual_inventory': 1,
			'abbr': args.company_abbr,
			'default_currency': args.currency,
			'country': args.country,
			'create_chart_of_accounts_based_on': 'Standard Template',
			'chart_of_accounts': args.chart_of_accounts,
			'domain': args.domain
		}
	]

	make_records(records)

#setup_wizard #3
def install_post_company_fixtures(args=None):
	records = [
		# Department
		{'doctype': 'Department', 'department_name': _('All Departments'), 'is_group': 1, 'parent_department': ''},
		{'doctype': 'Department', 'department_name': _('Accounts'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Marketing'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Sales'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Purchase'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Operations'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Production'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Dispatch'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Customer Service'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Human Resources'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Management'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Quality Management'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Research & Development'), 'parent_department': _('All Departments'), 'company': args.company_name},
		{'doctype': 'Department', 'department_name': _('Legal'), 'parent_department': _('All Departments'), 'company': args.company_name},
		# Marketplace
		{'doctype': 'Marketplace Settings', 'company': args.company_name },
	]

	make_records(records)

#setup_wizard #4
def install_defaults(args=None):
# Price Lists
	records = [
		{ "doctype": "Price List", "price_list_name": _("Standard Buying"), "enabled": 1, "buying": 1, "selling": 0, "currency": args.currency },
		{ "doctype": "Price List", "price_list_name": _("Standard Selling"), "enabled": 1, "buying": 0, "selling": 1, "currency": args.currency },
	]
	make_records(records)
# enable default currency
	frappe.db.set_value("Currency", args.get("currency"), "enabled", 1)
# system settings
	system_settings = frappe.get_doc("System Settings")
	system_settings.email_footer_address = args.get("company_name")
	system_settings.float_precision = "2"
	system_settings.currency_precision = "2"
	system_settings.enable_chat = "0"
	system_settings.allow_login_using_mobile_number = "1"
	system_settings.allow_login_using_user_name = "1"
	system_settings.allow_error_traceback = "0"
	system_settings.two_factor_method = "Email"
	system_settings.save()
# global defaults
	global_defaults = frappe.get_doc("Global Defaults", "Global Defaults")
	current_fiscal_year = frappe.get_all("Fiscal Year")[0]

	global_defaults.update({
		'current_fiscal_year': current_fiscal_year.name,
		'default_currency': args.get('currency'),
		'default_company':args.get('company_name')	,
		"country": args.get("country"),
		'default_distance_unit': "Kilometer",
		'hide_currency_symbol': "No"
	})

	global_defaults.save()
# domain settings
	domain_settings = frappe.get_single('Domain Settings')
	domain_settings.set_active_domains(args.get('domains'))
# stock settings
	stock_settings = frappe.get_doc("Stock Settings")
	stock_settings.item_naming_by = "Item Code"
	stock_settings.valuation_method = "FIFO"
	stock_settings.default_warehouse = frappe.db.get_value('Warehouse', {'warehouse_name': _('Stores')})
	stock_settings.auto_indent = 0
	stock_settings.auto_insert_price_list_rate_if_missing = 1
	stock_settings.automatically_set_serial_nos_based_on_fifo = 1
	stock_settings.set_qty_in_transactions_based_on_serial_no_input = 1
	stock_settings.item_group = "Products"
	stock_settings.show_barcode_field = 1
	stock_settings.stock_uom = "Unit"
	stock_settings.save()
# selling_settings
	selling_settings = frappe.get_doc("Selling Settings")
	selling_settings.set_default_customer_group_and_territory()
	selling_settings.territory = "Indonesia"
	selling_settings.cust_master_name = "Customer Name"
	selling_settings.so_required = "No"
	selling_settings.dn_required = "No"
	selling_settings.allow_multiple_items = 1
	selling_settings.sales_update_frequency = "Each Transaction"
	selling_settings.campaign_naming_by = "Campaign Name"
	selling_settings.save()
# buying_settings
	buying_settings = frappe.get_doc("Buying Settings")
	buying_settings.supp_master_name = "Supplier Name"
	buying_settings.supplier_group = "Distributor"
	buying_settings.po_required = "No"
	buying_settings.pr_required = "No"
	buying_settings.maintain_same_rate = 1
	buying_settings.allow_multiple_items = 1
	buying_settings.save()
# hr_settings
	hr_settings = frappe.get_doc("HR Settings")
	hr_settings.emp_created_by = "Naming Series"
	hr_settings.leave_approval_notification_template = _("Leave Approval Notification")
	hr_settings.leave_status_notification_template = _("Leave Status Notification")
	hr_settings.retirement_age = "60"
	hr_settings.emp_created_by = _("Employee Number")
	hr_settings.email_salary_slip_to_employee = 0
	hr_settings.stop_birthday_reminders = 1
	hr_settings.save()
# manufacturing_settings
	manufacturing_settings = frappe.get_doc("Manufacturing Settings")
	manufacturing_settings.allow_overtime = 1
	manufacturing_settings.save()
# pos_settings
	pos_settings = frappe.get_doc("POS Settings")
	pos_settings.use_pos_in_offline_mode = 1
	pos_settings.save()
# website_settings
	website_settings = frappe.get_doc("Website Settings")
	website_settings.chat_welcome_message = "Hi, apa yang bisa kami bantu?"
	website_settings.chat_room_name = "Bantuan"
	website_settings.chat_enable_from = "07:00:00"
	website_settings.chat_enable_to = "18:00:00"
	website_settings.hide_footer_signup = 1
	website_settings.disable_signup = 1
	website_settings.save()
# marketplace_settings
	marketplace_settings = frappe.get_doc("Marketplace Settings")
	marketplace_settings.marketplace_url = "https://puniamarket.com/"
	marketplace_settings.disable_marketplace = 1
	marketplace_settings.save()
# homepage_description
	homepage_description = frappe.get_doc("Homepage")
	# homepage_description.tag_line = _("UMKM Indonesia")
	homepage_description.tag_line = args.company_name
	homepage_description.description = _("Bersama Punia untuk kemajuan UKM Indonesia")
	homepage_description.save()
# bank account
	if args.bank_account:
		company_name = args.company_name
		bank_account_group =  frappe.db.get_value("Account",
			{"account_type": "Bank", "is_group": 1, "root_type": "Asset",
				"company": company_name})
		if bank_account_group:
			bank_account = frappe.get_doc({
				"doctype": "Account",
				'account_name': args.bank_account,
				'parent_account': bank_account_group,
				'is_group':0,
				'company': company_name,
				"account_type": "Bank",
			})
			try:
				doc = bank_account.insert()

				frappe.db.set_value("Company", args.company_name, "default_bank_account", bank_account.name, update_modified=False)

			except RootNotEditable:
				frappe.throw(_("Bank account cannot be named as {0}").format(args.bank_account))
			except frappe.DuplicateEntryError:
				# bank account same as a CoA entry
				pass
# add dashboard
	add_dashboards()
# Shopping cart: needs price lists
	records = [
		{
			"doctype": "Shopping Cart Settings",
			"enabled": 1,
			'company': args.company_name,
			'price_list': frappe.db.get_value("Price List", {"selling": 1}),
			'default_customer_group': _("Individual"),
			'quotation_series': "QTN-OL-.YYYY.MM.",
			'show_stock_availability': 1,
			'show_quantity_in_website': 1,
			'show_price': 1,
			'show_contact_us_button': 1
		},
	]

	make_records(records)

def add_uom_data():
	# add UOMs
	uoms = json.loads(open(frappe.get_app_path("erpnext", "setup", "setup_wizard", "data", "uom_data.json")).read())
	for d in uoms:
		if not frappe.db.exists('UOM', _(d.get("uom_name"))):
			uom_doc = frappe.get_doc({
				"doctype": "UOM",
				"uom_name": _(d.get("uom_name")),
				"name": _(d.get("uom_name")),
				"must_be_whole_number": d.get("must_be_whole_number")
			}).insert(ignore_permissions=True)

	# bootstrap uom conversion factors
	uom_conversions = json.loads(open(frappe.get_app_path("erpnext", "setup", "setup_wizard", "data", "uom_conversion_data.json")).read())
	for d in uom_conversions:
		if not frappe.db.exists("UOM Category", _(d.get("category"))):
			frappe.get_doc({
				"doctype": "UOM Category",
				"category_name": _(d.get("category"))
			}).insert(ignore_permissions=True)

		if not frappe.db.exists("UOM Conversion Factor", {"from_uom": _(d.get("from_uom")), "to_uom": _(d.get("to_uom"))}):
			uom_conversion = frappe.get_doc({
				"doctype": "UOM Conversion Factor",
				"category": _(d.get("category")),
				"from_uom": _(d.get("from_uom")),
				"to_uom": _(d.get("to_uom")),
				"value": d.get("value")
			}).insert(ignore_permissions=True)

def add_dashboards():
	from erpnext.setup.setup_wizard.data.dashboard_charts import get_company_for_dashboards

	if not get_company_for_dashboards():
		return

	from erpnext.setup.setup_wizard.data.dashboard_charts import get_default_dashboards
	from frappe.modules.import_file import import_file_by_path

	dashboard_data = get_default_dashboards()

	# create account balance timeline before creating dashbaord charts
	doctype = "dashboard_chart_source"
	docname = "account_balance_timeline"
	folder = os.path.dirname(frappe.get_module("erpnext.accounts").__file__)
	doc_path = os.path.join(folder, doctype, docname, docname) + ".json"
	import_file_by_path(doc_path, force=0, for_sync=True)

	make_records(dashboard_data["Charts"])
	make_records(dashboard_data["Dashboards"])

def get_fy_details(fy_start_date, fy_end_date):
	start_year = getdate(fy_start_date).year
	if start_year == getdate(fy_end_date).year:
		fy = cstr(start_year)
	else:
		fy = cstr(start_year) + '-' + cstr(start_year + 1)
	return fy
