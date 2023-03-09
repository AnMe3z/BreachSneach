// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

contract BreachSneach {
    uint public snitchPrice = 10000000000000000 wei;
    address payable public owner;

    constructor(){
        owner = payable(msg.sender);
    }

    function snitch() payable public {
        require(msg.value >= snitchPrice, "You're too broke for this");
        
    }
    
    function withdraw() public {
        require(address(this).balance >= snitchPrice, "Not enough funds to withdraw");
        require(msg.sender == owner, "You aren't the owner");

        owner.transfer(address(this).balance);
    }
}
