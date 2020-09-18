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
				'status': _('Setting up territory'),
				'fail_msg': _('Failed to setup territory'),
				'tasks': [
					{
						'fn': setup_territory,
						'args': args,
						'fail_msg': _("Failed to setup territory")
					},
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
					},
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
				'status': _('Setting up defaults'),
				'fail_msg': 'Failed to set defaults',
				'tasks': [
					{
						'fn': setup_defaults,
						'args': args,
						'fail_msg': _("Failed to setup defaults")
					}
				]
			},
			{
				'status': _('Setting up commerce defaults'),
				'fail_msg': 'Failed to set commerce defaults',
				'tasks': [
					{
						'fn': setup_commerce,
						'args': args,
						'fail_msg': _("Failed to setup commerce defaults")
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

def setup_territory(args):
	fixtures.install_territory(args.get('country'))

def setup_company(args):
	fixtures.install_company(args)
	fixtures.install_post_company_fixtures(args)

def setup_website(args):
	company_setup.create_website(args)
	company_setup.create_email_digest()
	company_setup.create_logo(args)

def setup_defaults(args):
	fixtures.install_defaults(frappe._dict(args))

def setup_commerce(args):
	fixtures.install_commerce(frappe._dict(args))

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


