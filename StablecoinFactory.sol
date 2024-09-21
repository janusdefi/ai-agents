// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StablecoinFactory is Ownable {
    struct Stablecoin {
        address tokenAddress;
        address collateralToken;
        uint256 targetPrice;
    }

    mapping(string => Stablecoin) public stablecoins;

    JanusMainProtocol public janusMainProtocol;

    event StablecoinCreated(string indexed name, address tokenAddress, address collateralToken, uint256 targetPrice);

    constructor(address _janusMainProtocol) {
        janusMainProtocol = JanusMainProtocol(_janusMainProtocol);
    }

    function createStablecoin(string memory name, address collateralToken, uint256 targetPrice) external onlyOwner {
        ERC20 stablecoin = new ERC20(name, name);
        stablecoins[name] = Stablecoin(address(stablecoin), collateralToken, targetPrice);
        emit StablecoinCreated(name, address(stablecoin), collateralToken, targetPrice);
    }

    function mintStablecoin(string memory name, uint256 amount) external {
        Stablecoin storage stablecoin = stablecoins[name];
        require(stablecoin.tokenAddress != address(0), "Stablecoin does not exist");

        janusMainProtocol.depositCollateral(stablecoin.collateralToken, amount);
        ERC20(stablecoin.tokenAddress).transfer(msg.sender, amount);
    }
}
