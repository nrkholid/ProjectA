from odoo import _, api, fields, models
from dateutil.relativedelta import relativedelta

class Partner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner'

    # Personal Information
    tanggal_lahir = fields.Date('Tanggal Lahir')
    umur = fields.Integer(compute='_compute_umur', string='Umur')
    
    @api.depends('tanggal_lahir')
    def _compute_umur(self):
        for rec in self:
            umur = relativedelta(fields.Date.context_today(self), rec.tanggal_lahir)
            rec.umur = umur.years
    
    nik = fields.Char('NIK', index = True, copy = False, tracking = True)
    jenis_kelamin = fields.Selection([
        ('laki', 'Laki - Laki'),
        ('perempuan', 'Perempuan')
    ], string='Jenis Kelamin', default = 'laki')
