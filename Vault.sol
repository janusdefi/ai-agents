// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Vault is Ownable {
    ERC20 public collateralToken;
    uint256 public yieldRate;

    mapping(address => uint256) public userBalances;

    event CollateralDeposited(address indexed user, uint256 amount);
    event YieldClaimed(address indexed user, uint256 amount);

    constructor(address _collateralToken, uint256 _yieldRate) {
        collateralToken = ERC20(_collateralToken);
        yieldRate = _yieldRate;
    }

    function depositCollateral(uint256 amount) external {
        collateralToken.transferFrom(msg.sender, address(this), amount);
        userBalances[msg.sender] += amount;
        emit CollateralDeposited(msg.sender, amount);
    }

    function claimYield() external {
        uint256 userBalance = userBalances[msg.sender];
        require(userBalance > 0, "No collateral deposited");

        uint256 yield = (userBalance * yieldRate) / 100;
        collateralToken.transfer(msg.sender, yield);
        emit YieldClaimed(msg.sender, yield);
    }
}
