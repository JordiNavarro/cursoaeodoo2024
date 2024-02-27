from odoo import models, fields

class SportsIssue(models.Model):
    _name = 'sports.issue'
    _description = 'Sports Issue'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    assistance = fields.Boolean(string='Assistance',help='Show if the issue has assitastance')
    state=fields.Selection(
        [('draft', 'Draft'),
          ('open', 'Open'),
          ('done','Done') ],
          string='State',
          default='draft')
    user_id = fields.Many2one('res.users', string='User')
    sequence = fields.Integer(string='Sequence',default=10)
    solution = fields.Html(string='Solution')
          