// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CornHubKernelsV2 is ERC20, Ownable {
    constructor() ERC20("CornHub Kernels", "CORN") {
        _mint(msg.sender, 800 * 10**decimals()); // 800 tokens with 18 decimals
    }
}
