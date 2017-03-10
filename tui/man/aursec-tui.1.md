% AURSEC-TUI(1) aursec user manuals
% Lukas Krismer and Bennett Piater
% March 10, 2017

# NAME
aursec-tui - interactive aursec-chain viewer

# SYNOPSIS
aursec-tui

# DESCRIPTION
Aursec-tui is an interactive viewer for the blocks in the aursec blockchain.

# INTERACTIVE COMMANDS

Up, k        
:   highlight 

Down, j
:   select previous block


# EXIT STATUS

0
: Success

1
: Failure 

# ENVIRONMENT

# FILES

# NOTES

# BUGS

# EXAMPLES

To mine 5 blocks
: $ aursec-chain mine blocks 5

To commit hash "hash123" of package "pkg1"
: $ aursec-chain commit-hash pkg1 hash123

To get hash of "pkg1"
: $ aursec-chain get-hash pkg1

# SEE ALSO
**aursec**(1), **aursec-hash**(1), **aursec**(7).

# COPYRIGHT
This is free software licensed under the Mozilla Public License, v. 2.0.
If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/
