% AURSEC-HASH(1) aursec user manuals
% Lukas Krismer and Bennett Piater
% November 21, 2016

# NAME
aursec-hash - hash AUR package sources

# SYNOPSIS
aursec-hash [*options*] [*BUILD_DIR* ...]

# Description
Hash package sources, get their id, and output both. If the package has VCS sources, download them with **makepkg** (to speed up a following build) and include them in the final hash. 

If *BUILD_DIR* is not set, or -, read from STDIN.

The *PKGBUILD* is sourced to get the most up-to-date id from \$pkgname-\$pkgver-\$pkgrel, and during the **makepkg** call for vcs source download. For security reasons, both happen within a **firejail**(1) sandbox, but manual verification prior to calling this script is recommended.

Output format:
: *PKG_ID* *HASH* one line per source folder.

# OPTIONS
-h, \--help
: Show this help message.

-v, \--verbose
: Show additional output.

-d, \--debug
: Show all individual hashes on stderr.

-n, \--novcs
: Do not download VCS sources, exit 71 instead.

# EXIT STATUS
0
: if OK

70
: if no valid build dir was given. A build dir must contain a *PKGBUILD* and a *.SRCINFO*

71
: if VCS sources were found, but may not be downloaded

In some cases, the exit status of the last program to fail is used.

# ENVIRONMENT

# FILES

# NOTES

# BUGS

# EXAMPLES
Hash a source folder:

    $ git clone aur@archlinux.org/foo.git
    $ aursec foo

Hash lots of sources at once:

    $ find ~/ABS/aur-packages -type d | aursec

# SEE ALSO
**aursec**(1), **aursec-chain**(1), **aursec**(7).

# COPYRIGHT
This is free software licensed under the Mozilla Public License, v. 2.0.
If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/
