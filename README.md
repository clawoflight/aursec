# AURSEC

[![MPL 2.0](https://img.shields.io/github/license/clawoflight/aursec.svg)](https://github.com/clawoflight/aursec/blob/master/LICENSE)
[![CircleCI](https://img.shields.io/circleci/project/github/clawoflight/aursec/master.svg)](https://circleci.com/gh/clawoflight/aursec)
[![Downloads](https://img.shields.io/github/downloads/clawoflight/aursec/total.svg)](https://github.com/clawoflight/aursec/releases)
[![AUR Version](https://img.shields.io/aur/version/aursec.svg)](https://aur.archlinux.org/packages/aursec)

> Blockchain-based security layer for the AUR

It's goal is to alleviate some of the AUR's security issues by building a hash database in a private Ethereum blockchain.

This repository contains several components:

- The primary program, [aursec](https://github.com/clawoflight/aursec/tree/master/aursec/)
- The Solidity code (Ethereum smart contract), in [Ethereum](https://github.com/clawoflight/aursec/tree/master/Ethereum)
- The paper 
- Our presentations

## Building

We manage and test the solidity code using [Populus](https://github.com/pipermerriam/populus), but end users don't need to install that.

The main program **is available in the [AUR](https://aur.archlinux.org/aursec)**.
To install it by hand, simply call `make install` in the `aursec` folder and create a system user and group named `aursec`.

You will need the following dependencies:

- `firejail`: required in `aursec-hash`.
- `geth`: to run the local blockchain.
- `pandoc`: to compile the man-pages.
- `vim`: for `xxd`, required in `aursec-chain`.
- `acpi`: to check charging status in `aursec-chain`.
- `bc`: required in `aursec-chain`.

## Using

Aursec can be used to verify sources by hand. We also provide a wrapper for `aursync` (from aurutils) which transparently calls `aursec`.
However, our hope is that the major AUR helpers will catch on and make themselves extensible, or integrate aursec directly.

In the mean time, you can use one like `bauerbill`, which supports custom hooks, and create one that calls aursec. We hope to provide example hooks for various AUR helpers in the future.

Before using the program, run `aursec-init` and ensure that `aursec-blockchain.service` is running and `aursec-blockchain-mine.timer` is enabled.

The basic usage is as follows:

- `aursec-hash` prints a package ID and hash to stdout, which can be piped to
- `aursec-verify-hashes`, which verifies packages against the blockchain using
- `aursec-chain`, which is a bash API for the blockchain component.
- `aursec` is a powerful convenience wrapper around these.

For more precise information, please read the man pages; their markdown sources are included [in this repository](https://github.com/clawoflight/aursec/tree/master/aursec/man).
Aursec(7) contains a thorough introduction into the use and design of this project.
