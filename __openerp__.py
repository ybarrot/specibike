# -*- coding: utf-8 -*-
##############################################################################
#    LICENCE TEMPORAIRE - EN COURS DE DEFINITION
#    Copyright (C) 2014  Reseau Certa yann.barrot@reseaucerta.org
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
	'name': "Specibike",
	'version': '1.0',
	'category': '',
	'license': 'AGPL-3', # A VALIDER	
	'description': """
Module de donnees pour Specibike				
====================================

Ce module peut être installé sans aucun autre module préalable. Il appelle les modules nécessaires.

Il comprend en particulier :
--------------------------------------------
  * les données de base : utilisateurs, employés					
  * les produits, catégories ...
  * les données d'inventaires
  * les bons de commande, factures
  * un paramétrage du site de vente en ligne

Il permet de travailler sur :
--------------------------------------------
  * CRM	: workflow de vente, équipe commerciale, campagnes marketing			
  * Comptabilité : impact comptable des opérations de vente (grand livre, bilan ...)
  * GRH : paie, recrutement, gestion des congés ...
  * Système d'information : intégration de la vente en ligne
 
				 
	""",
	'author': "Réseau Certa",
	'website': "http://www.reseaucerta.org/",

	# any module necessary for this one to work correctly
	'depends': [
		'base',
		'mail',
		'contacts',
		'l10n_fr',
		'account_accountant',
		'stock',
		'sale',
		'crm',
		'purchase',
		'hr',
		'hr_expense',
		'hr_holidays',
		'hr_recruitment',
		'hr_evaluation',
		'hr_timesheet',
		'hr_payroll',
		'l10n_fr_hr_payroll',
		'knowledge',
		'website',
		'website_sale'
		],

	# always loaded
	'data': [
		'specibike_pre_install.yml',
		'configuration.xml',#dates		
		'hr.department.csv',
		'hr.employee.category.csv',
		'crm.case.section.csv',
		'res.partner.csv',
		'res.users.csv',
		'res_partner_img.xml',		
		'hr.employee.csv',
		'hr_employee.xml',		
		'2round/hr.department.csv',		
		'2round/crm.case.section.csv',		
		'product.category.csv',
		'product.public.category.csv',
		'product.product.csv',
		#stocks
		'stock_warehouse.xml',	
		'stock_inventory.xml',#date	
		'stock.inventory.line.csv',
		'stock_inventory_validate.xml',
		#devis & factures
		'sale.order.csv',#sans date => date d'installation du module
		#'date/sale.order.csv', #avec date à definir dans le fichier - !! rester dans le mois en cours ou modifier les périodes dans sale_order_workflow => pay & reconcile
		'sale.order.line.csv',		
		'sale_order_workflow.xml',
		#livraison
		'procurement_order.xml',
		#site web
		'website.xml',
		'website_product.xml',
		#contrats
		'hr_contract.xml',
						
	],
	# only loaded in demonstration mode
	'demo': [				
	],
	'installable': True,
}
