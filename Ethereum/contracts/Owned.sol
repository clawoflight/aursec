pragma solidity ^0.4.0;

/**
 * @title Base class for contracts with an owner.
 * @author Bennett Piater
 */
contract Owned {
    address public owner;

    event ContractClosed(string description);

    function Owned() {
        owner = msg.sender;
    }

    /// Modifier that restricts functions to the owner
    modifier onlyOwner {
        if (msg.sender != owner) throw;
        _;
    }

    /**
     * @notice Transfer ownership of this contract to the given owner
     *
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) onlyOwner {
        owner = newOwner;
    }

    /**
     * @notice Self-destruct this contract. It will be read-only in the future.
     */
    function close() onlyOwner {
        ContractClosed("The owner of this contract decided to close it.");
        selfdestruct(owner);
    }
}
