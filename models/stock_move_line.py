# STeSI Consulting - Francesco Pranzo
# License OPL-1 (https://www.odoo.com/documentation/user/19.0/legal/licenses/licenses.html).
from odoo import models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _apply_putaway_strategy(self):
        # `qty_done` was renamed to `quantity` in Odoo 17.
        not_picked = self.filtered(lambda l: not l.quantity or not l.picking_id)
        return super(StockMoveLine, not_picked)._apply_putaway_strategy()
