// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract JanusMainProtocol is Ownable {
    struct Vault {
        address collateralToken;
        uint256 collateralAmount;
        uint256 yieldRate;
    }

    mapping(address => Vault) public vaults;
    mapping(address => uint256) public userBalances;

    ERC20 public janusToken;

    event VaultCreated(address indexed vaultAddress, address collateralToken, uint256 yieldRate);
    event CollateralDeposited(address indexed user, address vaultAddress, uint256 amount);
    event YieldClaimed(address indexed user, uint256 amount);

    constructor(address _janusToken) {
        janusToken = ERC20(_janusToken);
    }

    function createVault(address collateralToken, uint256 yieldRate) external onlyOwner {
        Vault storage vault = vaults[collateralToken];
        vault.collateralToken = collateralToken;
        vault.yieldRate = yieldRate;
        emit VaultCreated(collateralToken, collateralToken, yieldRate);
    }

    function depositCollateral(address collateralToken, uint256 amount) external {
        require(vaults[collateralToken].collateralToken != address(0), "Vault does not exist");
        ERC20(collateralToken).transferFrom(msg.sender, address(this), amount);
        userBalances[msg.sender] += amount;
        vaults[collateralToken].collateralAmount += amount;
        emit CollateralDeposited(msg.sender, collateralToken, amount);
    }

    function claimYield(address collateralToken) external {
        uint256 userBalance = userBalances[msg.sender];
        require(userBalance > 0, "No collateral deposited");
        
        uint256 yield = (userBalance * vaults[collateralToken].yieldRate) / 100;
        janusToken.transfer(msg.sender, yield);
        emit YieldClaimed(msg.sender, yield);
    }
}
