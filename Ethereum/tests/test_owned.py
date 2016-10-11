# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright © 2016-2017 Lukas Krismer and Bennett Piater.

def test_owner(chain):
    owned = chain.get_contract('Owned')
    owner = owned.call().owner()


def test_transfer_ownership(chain):
    owned = chain.get_contract('Owned')
    owner = owned.call().owner()

    owned.transact().transferOwnership('0x82a278b3f59620000007d9ee9eef472ee55b42f1')
    assert owned.call().owner() == '0x82a278b3f59620000007d9ee9eef472ee55b42f1'
