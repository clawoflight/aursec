% AURSEC-TUI(1) aursec user manuals
% Lukas Krismer and Bennett Piater
% March 10, 2017

# NAME
aursec-tui - interactive aursec-blockchain viewer

# SYNOPSIS
aursec-tui

# DESCRIPTION
Aursec-tui is a free urwid-based interactive viewer for the blocks in the aursec blockchain.

# INTERACTIVE COMMANDS

Up, k        
:   Highlight next block, if you highlighted the current block go back to settings

Down, j
:   Highlight previous block

R, r
:   Refresh the view with the current settings and/or load older blocks

Q, q
:   Quit

# INTERACTIVE SETTINGS:

only transactions
:   Shows just blocks with transactions after the next refresh 

only mine
:   Shows just blocks which where mined by you after the next refresh

# BUTTON

refresh
:   See R, r in interactive commands

# COLUMNS

Nr
:   Number of the block

Hash
:   Hash of the block

Miner
:   User hash of the user who mined the block

Time
:   Time when the block was mined

Transactions
:   Shows all Transactions of an block

# COPYRIGHT
This is free software licensed under the Mozilla Public License, v. 2.0.
If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/
