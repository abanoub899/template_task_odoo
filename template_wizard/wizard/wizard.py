from odoo import models, fields, api
from odoo.tools import float_round
from odoo.exceptions import ValidationError
import time
import pytz
import dateutil.parser
import datetime
import xlsxwriter


class TemplateWizard(models.TransientModel):
    _name = 'template.wizard'
    name = fields.Char('Name')
    date_from = fields.Date('From', required=True)
    date_to = fields.Date('To', required=True)
