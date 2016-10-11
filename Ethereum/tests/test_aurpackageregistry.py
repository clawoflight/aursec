def test_empty_consensus(chain):
    registry = chain.get_contract("AURPackageRegistry")
    yaourt_hash, submissions = registry.call().getCurrentConsensus("yaourt")
    assert yaourt_hash == ""
    assert submissions == 0

def test_submit_hash_success(chain):
    registry = chain.get_contract("AURPackageRegistry")
    registry.transact().submitPkgHash("yaourt", "asdf")
    yaourt_hash, submissions = registry.call().getCurrentConsensus("yaourt")
    assert yaourt_hash == "asdf"
    assert submissions == 1

def test_submit_same_hash_twice(chain):
    registry = chain.get_contract("AURPackageRegistry")
    registry.transact().submitPkgHash("yaourt", "asdf")
    registry.transact().submitPkgHash("yaourt", "jklö")
    yaourt_hash, submissions = registry.call().getCurrentConsensus("yaourt")
    assert yaourt_hash == "asdf"
    assert submissions == 1
