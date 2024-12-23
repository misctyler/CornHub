// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

contract cornhubSelects is ERC721URIStorage, Ownable {
    uint256 private _tokenIdCounter;
    mapping(address => bool) private _owners;
    string[] private _tokenURIs;
    bool public publicMintActive;
    string public publicMintTokenURI;
    address public immutable linkedNFTContract;

    constructor(address initialOwner) ERC721("Cornhub Selects", "HUBS") Ownable(initialOwner) {
        _tokenIdCounter = 1;
        _owners[initialOwner] = true; 
        linkedNFTContract = 0xDBB09CEd27B571885A1B4EBd093587eDC00eae20;
    }

    modifier onlyOwners() {
        require(_owners[msg.sender], "Caller is not an owner");
        _;
    }

    modifier onlyNFTOwner() {
        require(IERC721(linkedNFTContract).balanceOf(msg.sender) > 0, "Caller does not own a required NFT");
        _;
    }

    function addOwner(address newOwner) public onlyOwner {
        _owners[newOwner] = true;
    }

    function removeOwner(address owner) public onlyOwner {
        require(owner != msg.sender, "Cannot remove self as owner");
        _owners[owner] = false;
    }

    function isOwner(address account) public view returns (bool) {
        return _owners[account];
    }

    function addTokenURI(string memory tokenURI) public onlyOwner {
        _tokenURIs.push(tokenURI);
    }

    function mintBatchNFT(address[] memory recipients, uint256 uriIndex) public onlyOwners {
        require(uriIndex < _tokenURIs.length, "Invalid URI index");

        for (uint256 i = 0; i < recipients.length; i++) {
            uint256 tokenId = _tokenIdCounter;
            _tokenIdCounter += 1;

            _mint(recipients[i], tokenId);
            _setTokenURI(tokenId, _tokenURIs[uriIndex]);
        }
    }

    function getTokenURIs() public view returns (string[] memory) {
        return _tokenURIs;
    }

    function setPublicMintState(bool isActive) public onlyOwner {
        publicMintActive = isActive;
    }

    function setPublicMintTokenURI(string memory tokenURI) public onlyOwner {
        publicMintTokenURI = tokenURI;
    }

    function publicMint() public onlyNFTOwner {
        require(publicMintActive, "Public minting is not active");
        require(bytes(publicMintTokenURI).length > 0, "Public mint token URI not set");

        uint256 tokenId = _tokenIdCounter;
        _tokenIdCounter += 1;

        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, publicMintTokenURI);
    }
}
