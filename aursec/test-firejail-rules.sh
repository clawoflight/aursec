#!/bin/bash
# Unit/Regression tests for the firejail rules.
# This script requires mksrcinfo from pkgbuild-introspection.
# shellcheck disable=SC1090,SC2154
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2016-2017 Lukas Krismer and Bennett Piater.
declare -a test_case_names failed_tests
declare -A pkgbuilds test_conditions cleanup_funcs

source /usr/share/makepkg/util.sh
colorize
# Output the firejail ruleset
plain "Testing the following firejail options:"
grep "readonly firejail_opts=" "$(which aursec-hash)"
grep "firejail " "$(which aursec-hash)"

################
# Define tests #
################
# Create a file in /tmp
name="disallow writes to /tmp"
test_case_names+=("$name")
test_conditions["$name"]="! stat /tmp/evil_file"
cleanup_funcs["$name"]="rm -f /tmp/evil_file"
pkgbuilds["$name"]="touch /tmp/evil_file"

# Create a file in $HOME
name="disallow writes to /home"
test_case_names+=("$name")
test_conditions["$name"]="! stat ~/evil_file"
cleanup_funcs["$name"]="rm -f ~/evil_file"
pkgbuilds["$name"]="touch ~/evil_file"

# Create a file in the directory of the pkgbuild
name="allow writes to the source folder"
test_case_names+=("$name")
test_conditions["$name"]="stat good_file"
cleanup_funcs["$name"]="rm -f good_file"
pkgbuilds["$name"]="touch good_file"

#################
# Execute tests #
#################
TMP_DIR="$(mktemp -d)"
cd_safe "$TMP_DIR"

msg "Executing tests..."
for test_case in "${test_case_names[@]}"; do
	msg2 "testing '$test_case'..."
	# Prepare the package.
	# The printf comand takes care of the minimal requirements,
	# so we need only add the minimum to the array.
	printf "pkgname=test\npkgver=0.1\npkgrel=1\narch=(any)\n" > PKGBUILD
	echo "${pkgbuilds[$test_case]}" >> PKGBUILD
	mksrcinfo >/dev/null

	# Run aursec-hash
	aursec-hash . >/dev/null
	# Check whether this test failed
	eval "${test_conditions[$test_case]}" >/dev/null 2>&1 || failed_tests+=("$test_case")
	# Clean up
	eval "${cleanup_funcs[$test_case]}" >/dev/null
	rm -rf ./* >/dev/null 2>&1
	rm -rf .* >/dev/null 2>&1
done
cd_safe /tmp
rm -rf "$TMP_DIR"

##########
# Finish #
##########
# Summary output. Exit 1 on error allows us to use 'git bisect run' to automatically find errors.
if ((${#failed_tests[@]})); then
	error "Some tests failed:"
	for t in "${failed_tests[@]}"; do
		msg2 "$t"
	done
	exit 1
else
	msg "Tests passed!"
	exit 0
fi
