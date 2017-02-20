% AURSEC(7) aursec user manuals
% Lukas Krismer and Bennett Piater
% November 21, 2016

# NAME
aursec - verify AUR package sources against hashes stored in a blockchain

# PROGRAMS
The following is just an overview, see the respective documentation for details.

aursec(1)
: Hash source folders and verify them against the blockchain.

aursec-chain(1)
: API for the blockchain.

aursec-hash(1)
: Ouput an ID and a hash for source folders.

aursec-parse-srcinfo(1)
: Extract helpful information from a *.SRCINFO*.

aursec-verify-hashes(1):
: Take IDs and hashes and compare them against the ones on the blockchain.

aursec-aursync-wrapper
: Use this instead of **aursync**(1) to integrate **aursec** with **aurutils**(7)

# PURPOSE
The open and insecure nature of the AUR makes a variety of attacks very easy to pull off. Aursec reduces the risks by creating a secure, distributed repository of hashes with package name, version and release as key.

Comparing the build files (*PKGBUILD*, *.SRCINFO*, *\*.patch*, *\*.install*) against those of other users makes targeted attacks much less feasible.

We also hash VCS sources, which is a huge security improvement since vcs packages don't have hashes in the *PKGBUILD*.

# NOTES
Most features of this toolkit require the blockchain to be running and periodical mining to be enabled. Please start and enable

    aursec-blockchain.service
    aursec-blockchain-mine.timer

before using them.

To use **aursec-aurbuild-wrapper** instead of **aurbuild**(1), add

    hash -p "$(which aursec-aurbuild-wrapper)" aurbuild
    alias -g aurbuild="$(which aursec-aurbuild-wrapper)"

to your *.zshrc*

To your *.bashrc*, or

    alias -g aurbuild="$(which aursec-aurbuild-wrapper)"

to your *.zshrc*. The former should also work when using **aursync**(1) because that's a bash script.

# BUGS

# SEE ALSO
**aursec**(1), **aursec-hash**(1), **aursec-chain**(1).

# COPYRIGHT
This is free software licensed under the Mozilla Public License, v. 2.0.
If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/
