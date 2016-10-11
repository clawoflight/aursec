# Tasks:

## Generate hash

`sha256deep -sbr FILES DIRS | sha256sum | cut -d " " -f 1` (sha256deep is in aur:hashdeep)
`sha256sum FILES | sha256sum | cut -d " " -f 1`

- PKGBUILD
- .SRCINFO
- patches
- install scripts
- entire VCS folder?

How should we parse the PKGBUILD to locate the patches and install scripts? (we could use `*install*` `*patch*` through globbing or `find`)
And what should we do about VCS data? It would need to be downloaded before our library is called...

Both would be solved by running "makepkg --verifysource" before invoking our library (or adding a corresponding option to the latter).
However, that would mean *executing the PKGBUILD* in order to complete the verification...
