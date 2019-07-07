from odoo import models, fields, api

class Clinic(models.Model):
    _name = 'clinic.menu'
    name = fields.Char(string='Clinic For Borning')
    doctor_name=fields.Many2one('res.users',ondelete='set null',string=" Doctor ",index=True)
    patient_name = fields.Many2one('res.partner',string="Patient Name")
    phone=fields.Char(required=True,string="Phone Number")
    Type=fields.Char(required=True,string="New / Backing")
    dateof=fields.Datetime(string="Date")
    city=fields.Char(string=" City ")
    role=fields.Integer(string='Role')
    Typeofill=fields.Char(string="have / Not have")
    
   
    
