// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

contract GoldTokenValidator is ERC721Holder {
    
    address constant GOLD_TOKEN_CONTRACT    = 0xDBB09CEd27B571885A1B4EBd093587eDC00eae20;
    uint8   constant GOLD_TOKEN_TRAIT_INDEX = 0;
    string  constant GOLD_TOKEN_TRAIT_VALUE = "Gold";
    
    function validateGoldTokenOwnership(address _owner) external view returns(bool) {
        ERC721Enumerable goldToken = ERC721Enumerable(GOLD_TOKEN_CONTRACT);
        uint256 tokenCount = goldToken.balanceOf(_owner);
        for (uint256 i = 0; i < tokenCount; i++) {
            uint256 tokenId = goldToken.tokenOfOwnerByIndex(_owner, i);
            if (goldToken.ownerOf(tokenId) == _owner) {
                if (keccak256(abi.encodePacked((goldToken.tokenURI(tokenId)))) == keccak256(
                    abi.encodePacked((string(abi.encodePacked('{"id":3,"description":"CornHub Represent","image":"https://misctyler.github.io/CornHub/images/moeda-gold.png","name":"Gold Kernel","attributes":[{"trait_type":"Coin","value":"Gold"}]}')))))) {
                    return true;
                }
            }
        }
        return false;
    }
}
