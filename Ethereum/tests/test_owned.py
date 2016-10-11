def test_owner(chain):
    owned = chain.get_contract('Owned')
    owner = owned.call().owner()


def test_transfer_ownership(chain):
    owned = chain.get_contract('Owned')
    owner = owned.call().owner()

    owned.transact().transferOwnership('0x82a278b3f59620000007d9ee9eef472ee55b42f1')
    assert owned.call().owner() == '0x82a278b3f59620000007d9ee9eef472ee55b42f1'
