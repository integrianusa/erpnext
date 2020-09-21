# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _

from .operations import install_fixtures as fixtures, company_setup, sample_data

def get_setup_stages(args=None):
	if frappe.db.sql("select name from tabCompany"):
		stages = [
			{
				'status': _('Wrapping up'),
				'fail_msg': _('Failed to login'),
				'tasks': [
					{
						'fn': fin,
						'args': args,
						'fail_msg': _("Failed to login")
					}
				]
			}
		]
	else:
		stages = [
			{
				'status': _('Installing domains'),
				'fail_msg': _('Failed to install domains'),
				'tasks': [
					{
						'fn': setup_domains,
						'args': args,
						'fail_msg': _("Failed to install domains")
					}
				]
			},
			{
				'status': _('Installing presets'),
				'fail_msg': _('Failed to install presets'),
				'tasks': [
					{
						'fn': stage_fixtures,
						'args': args,
						'fail_msg': _("Failed to install presets")
					}
				]
			},
			{
				'status': _('Setting up groups and types'),
				'fail_msg': _('Failed to install groups and types'),
				'tasks': [
					{
						'fn': setup_groups_and_types,
						'args': args,
						'fail_msg': _("Failed to setup groups and types")
					}
				]
			},
			{
				'status': _('Setting up territory'),
				'fail_msg': _('Failed to setup territory'),
				'tasks': [
					{
						'fn': setup_territory,
						'args': args,
						'fail_msg': _("Failed to setup territory")
					}
				]
			},
			{
				'status': _('Setting up company'),
				'fail_msg': _('Failed to setup company'),
				'tasks': [
					{
						'fn': setup_company,
						'args': args,
						'fail_msg': _("Failed to setup company")
					}
				]
			},
			{
				'status': _('Setting up website'),
				'fail_msg': _('Failed to setup website'),
				'tasks': [
					{
						'fn': setup_website,
						'args': args,
						'fail_msg': _("Failed to setup website")
					}
				]
			},
			{
				'status': _('Setting up system settings'),
				'fail_msg': 'Failed to set system settings',
				'tasks': [
					{
						'fn': setup_system_settings,
						'args': args,
						'fail_msg': _("Failed to setup system settings")
					}
				]
			},
			{
				'status': _('Setting up global defaults'),
				'fail_msg': 'Failed to set global defaults',
				'tasks': [
					{
						'fn': setup_global_defaults,
						'args': args,
						'fail_msg': _("Failed to setup global defaults")
					}
				]
			},
			{
				'status': _('Setting up domain settings'),
				'fail_msg': 'Failed to set domain settings',
				'tasks': [
					{
						'fn': setup_domain_settings,
						'args': args,
						'fail_msg': _("Failed to setup domain settings")
					}
				]
			},
			{
				'status': _('Setting up accounting'),
				'fail_msg': 'Failed to set accounting',
				'tasks': [
					{
						'fn': setup_accounting,
						'args': args,
						'fail_msg': _("Failed to setup accounting")
					}
				]
			},
			{
				'status': _('Setting up stock'),
				'fail_msg': 'Failed to set stock',
				'tasks': [
					{
						'fn': setup_stock,
						'args': args,
						'fail_msg': _("Failed to setup stock")
					}
				]
			},
			{
				'status': _('Setting up selling'),
				'fail_msg': 'Failed to set selling',
				'tasks': [
					{
						'fn': setup_selling,
						'args': args,
						'fail_msg': _("Failed to setup selling")
					}
				]
			},
			{
				'status': _('Setting up buying'),
				'fail_msg': 'Failed to set buying',
				'tasks': [
					{
						'fn': setup_buying,
						'args': args,
						'fail_msg': _("Failed to setup buying")
					}
				]
			},
			{
				'status': _('Setting up hr'),
				'fail_msg': 'Failed to set hr',
				'tasks': [
					{
						'fn': setup_hr,
						'args': args,
						'fail_msg': _("Failed to setup hr")
					}
				]
			},
			{
				'status': _('Setting up manufacturing'),
				'fail_msg': 'Failed to set manufacturing',
				'tasks': [
					{
						'fn': setup_manufacturing,
						'args': args,
						'fail_msg': _("Failed to setup manufacturing")
					}
				]
			},
			{
				'status': _('Setting up pos'),
				'fail_msg': 'Failed to set pos',
				'tasks': [
					{
						'fn': setup_pos,
						'args': args,
						'fail_msg': _("Failed to setup pos")
					}
				]
			},
			{
				'status': _('Setting up other features'),
				'fail_msg': 'Failed to set commerce',
				'tasks': [
					{
						'fn': setup_other_features,
						'args': args,
						'fail_msg': _("Failed to setup other features")
					}
				]
			},
			{
				'status': _('Setting domain'),
				'fail_msg': 'Failed to set domain',
				'tasks': [

					{
						'fn': set_active_domains,
						'args': args,
						'fail_msg': _("Failed to add Domain")
					}
				]
			},
			{
				'status': _('Wrapping up'),
				'fail_msg': _('Failed to login'),
				'tasks': [
					{
						'fn': fin,
						'args': args,
						'fail_msg': _("Failed to login")
					}
				]
			}
		]

	return stages

def setup_domains(args):
	fixtures.install_domains(args.get('country'))

def stage_fixtures(args):
	fixtures.install(args.get('country'))

def setup_groups_and_types(args):
	fixtures.install_group_and_types(args)

def setup_territory(args):
	fixtures.install_territory(args.get('country'))

def setup_company(args):
	fixtures.install_company(args)
	fixtures.install_post_company_fixtures(args)

def setup_website(args):
	company_setup.create_website(args)
	company_setup.create_email_digest()
	company_setup.create_logo(args)
	fixtures.setup_website(args)

def setup_system_settings(args):
	fixtures.install_system_settings(frappe._dict(args))

def setup_global_defaults(args):
	fixtures.install_global_defaults(frappe._dict(args))

def setup_domain_settings(args):
	fixtures.install_domain_settings(frappe._dict(args))

def setup_accounting(args):
	fixtures.install_accounting(frappe._dict(args))

def setup_stock(args):
	fixtures.install_stock(frappe._dict(args))

def setup_selling(args):
	fixtures.install_selling(frappe._dict(args))

def setup_buying(args):
	fixtures.install_buying(frappe._dict(args))

def setup_hr(args):
	fixtures.install_hr(frappe._dict(args))

def setup_manufacturing(args):
	fixtures.install_manufacturing(frappe._dict(args))

def setup_pos(args):
	fixtures.install_pos(frappe._dict(args))

def setup_other_features(args):
	fixtures.install_other_features(frappe._dict(args))

def set_active_domains(args):
	domain_settings = frappe.get_single('Domain Settings')
	domain_settings.set_active_domains(args.get('domains'))

def fin(args):
	frappe.local.message_log = []
	login_as_first_user(args)

	make_sample_data(args.get('domains'))

def make_sample_data(domains):
	try:
		sample_data.make_sample_data(domains)
	except:
		# clear message
		if frappe.message_log:
			frappe.message_log.pop()
		pass

def login_as_first_user(args):
	if args.get("email") and hasattr(frappe.local, "login_manager"):
		frappe.local.login_manager.login_as(args.get("email"))


# Only for programmatical use
def setup_complete(args=None):
	stage_fixtures(args)
	setup_company(args)
	setup_website(args)
	setup_defaults(args)
	set_active_domains(args)
	fin(args)


