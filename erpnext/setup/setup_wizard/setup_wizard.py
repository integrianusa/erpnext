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
				'status': _('Setting company fixtures'),
				'fail_msg': 'Failed to set company fixtures',
				'tasks': [
					{
						'fn': setup_post_company_fixtures,
						'args': args,
						'fail_msg': _("Failed to setup post company fixtures")
					}
				]
			},
			{
				'status': _('Setting defaults'),
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
				'status': _('Creating website'),
				'fail_msg': 'Failed to create website',
				'tasks': [
					{
						'fn': create_website,
						'args': args,
						'fail_msg': _("Failed to create website")
					}
				]
			},
			{
				'status': _('Set email digest'),
				'fail_msg': 'Failed to set email digest',
				'tasks': [
					{
						'fn': set_email_digest,
						'args': args,
						'fail_msg': _("Failed to set email digest")
					}
				]
			},
			{
				'status': _('Setting logo'),
				'fail_msg': 'Failed to set logo',
				'tasks': [
					{
						'fn': set_logo,
						'args': args,
						'fail_msg': _("Failed to set logo")
					}
				]
			},
			{
				'status': _('Adding domain'),
				'fail_msg': 'Failed to add domain',
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

def stage_fixtures(args):
	fixtures.install(args.get('country'))

def setup_company(args):
	fixtures.install_company(args)

def setup_post_company_fixtures(args):
	fixtures.install_post_company_fixtures(args)

def setup_defaults(args):
	fixtures.install_defaults(frappe._dict(args))

def create_website(args):
	company_setup.create_website(args)

def set_email_digest(args):
	company_setup.create_email_digest()

def set_logo(args):
	company_setup.create_logo(args)

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
	setup_post_company_fixtures(args)
	setup_defaults(args)
	create_website(args)
	set_email_digest(args)
	set_logo(args)	
	fin(args)


