/******************************************************************************
*** Submitted for verification at blockscout.com on 2021-05-15 02:01:48.212715Z
*******************************************************************************/
pragma solidity ^0.4.24;

// tyler is cool and does cool things sometimes
// like and subscribe

contract Token { 
    function transfer(address receiver, uint amount) public; 
    function balanceOf(address tokenOwner) public constant returns (uint balance);
}
 interface ERC20 {
    function transfer(address to, uint256 value) external;
    function transferFrom(address from, address to, uint256 value) external;
    function balanceOf(address tokenOwner)  external returns (uint balance);
}
contract Ownable {
  address public owner;
  function Ownable() {
    owner = msg.sender;
    } 
  modifier onlyOwner() {
    if (msg.sender != owner) {
      revert();
    }
    _;
  }
  function yeetOwnership(address newOwner) onlyOwner {
    if (newOwner != address(0)) {
      owner = newOwner;
    }
  }
}
contract tylersCryptoCannon is Ownable{
    function checkAmmo(address _tokenAddr) public view returns(uint) {
            return (ERC20(_tokenAddr).balanceOf(this));
    }     
    function fireWhenReady(address _tokenAddr, address[] _frens)
        onlyOwner
            returns (uint256) {
                uint256 _payout = ERC20(_tokenAddr).balanceOf(this)/_frens.length;
                uint256 i = 0;
                while (i < _frens.length) {
                    ERC20(_tokenAddr).transfer(_frens[i], _payout);
                    i += 1;
                }
            return (i);
            }
}   
