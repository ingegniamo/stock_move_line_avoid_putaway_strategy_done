# Skip Putaway Strategy on Picked Move Lines

[![License: OPL-1](https://img.shields.io/badge/license-OPL-1-F1972B.svg)](https://github.com/ingegniamo/stock_move_line_avoid_putaway_strategy_done)

Skips the putaway strategy for move lines that already carry a picked quantity, so a manually chosen destination location is not overwritten.

## Features

- Override of _apply_putaway_strategy restricted to lines with no quantity or no transfer

## Installation

Add the module to the addons path and install it from **Apps**.

## Technical Information

| | |
|---|---|
| Odoo version | 19.0 |
| Module version | 19.0.1.0.0 |
| License | OPL-1 |
| Depends | `stock` |

## Changelog

### 19.0.1.0.0

- Migration from Odoo 17.0 to Odoo 19.0

## Credits

**Authors**

* STeSI Consulting

**Contributors**

* Francesco Pranzo — pranzo.f@stesi.consulting
