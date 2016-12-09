% AURSEC(1) aursec user manuals
% Lukas Krismer and Bennett Piater
% November 21, 2016

# NAME
aursec - verify AUR package sources against hashes stored in a blockchain

# SYNOPSIS
aursec [*options*] [*BUILD_DIR* ...]

# Description
Verify package sources by checking their hashes against versions stored in a blockchain. Whichever hash was submitted by the most people wins.

If *BUILD_DIR* is not set, or -, read from STDIN.

This is just convenience glue for a pipeline of **aursec-hash**(1), **aursec-verify-hashes**(1) and **aursec-chain**(1) with fancy output and user interaction.

# OPTIONS
-h, \--help
: Show this help message.

-v, \--verbose
: Enable additional output.

-c, \--check-only
: Never submit hashes to the blockchain.

-s, \--status-only
: Only output critical errors and never prompt the user.

# STATES
- no hash in the blockchain: prompt
- hash below threshold: prompt
- hash above threshold and match: exit 0
- hash above threshold and on match: exit != 0

# EXIT STATUS
0
: if OK,

64
: if the initialization failed,

65
: if there was a problem contacting the chain,

66
: if no hash was found,

67
: if a hash was found, but it doesn't match the consensus.

In some cases, the exit status of the last program to fail is used.

# ENVIRONMENT

# FILES

# NOTES

# BUGS

# EXAMPLES

Verify sources against the blockchain:

    $ git clone aur@archlinux.org/foo.git
    $ aursec foo

Verify lots of sources at once:

    $ find ~/ABS/aur-packages -type d | aursec


# SEE ALSO
**aursec-hash**(1), **aursec-chain**(1), **aursec**(7).

# COPYRIGHT
This is free software licensed under the Mozilla Public License, v. 2.0.
If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/
