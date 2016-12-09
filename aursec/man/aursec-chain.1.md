% AURSEC-CHAIN(1) aursec user manuals
% Lukas Krismer and Bennett Piater
% November 21, 2016

# NAME
aursec-chain - api for the aursec blockchain

# SYNOPSIS
aursec-chain [*options*] [*commands*]

# Description
Aursec-chain is the bash API for aursec's private Ethereum blockchain.
It can be used to get or commit hashes for specific package IDs and to control mining.

It interfaces with the JSON-RPC.

# OPTIONS

-h, \--help
:   Show usage message.

-v, \--verbose      
:   Show additional output

-d, \--debug      
:   Show debug output like the line number where the script failed.


# COMMANDS

mine start        
:   Starts mining with the coinbase account

mine stop         
:   Stops mining with the coinbase account

mine blocks *NUMBER*     
:   mines min. *NUMBER* Blocks with the coinbase account

get-hash  *STRING*       
:   Gets current consensus-hash and number of commits of package *STRING* 

commit-hash *STRING1 STRING2*  
:   Commit new hash *STRING2* of package *STRING1* in the blockchain


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
