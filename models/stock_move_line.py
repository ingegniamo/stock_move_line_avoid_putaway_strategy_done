

from odoo import _, api, Command, fields, models





class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _apply_putaway_strategy(self):
        self = self.filtered(lambda l: l.qty_done == 0 or not l.picking_id)
        return super(StockMoveLine,self)._apply_putaway_strategy()