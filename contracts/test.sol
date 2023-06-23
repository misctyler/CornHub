pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenVesting {
    IERC20 public vestingToken;
    IERC20 public lpToken;
    uint256 public totalDeposited;
    mapping(address => uint256) public vestingBalances;
    mapping(address => uint256) public releasedBalances;
    uint256 public startTime;
    
    constructor(IERC20 _vestingToken, IERC20 _lpToken) {
        vestingToken = _vestingToken;
        lpToken = _lpToken;
    }
    
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lpToken.balanceOf(msg.sender) >= amount, "Insufficient LP tokens");
        require(lpToken.allowance(msg.sender, address(this)) >= amount, "Token allowance too low");
        
        uint256 existingBalance = vestingBalances[msg.sender];
        vestingBalances[msg.sender] = existingBalance + amount;
        totalDeposited += amount;
        
        lpToken.transferFrom(msg.sender, address(this), amount);
        
        if (startTime == 0) {
            startTime = block.timestamp;
        }
    }
    
    function release() external {
        require(vestingBalances[msg.sender] > 0, "No tokens to release");
        
        uint256 totalVestingTime = block.timestamp - startTime;
        uint256 vestedAmount = (vestingBalances[msg.sender] * totalVestingTime) / 1 years;
        uint256 unreleasedAmount = vestedAmount - releasedBalances[msg.sender];
        require(unreleasedAmount > 0, "No tokens to release");
        
        releasedBalances[msg.sender] = vestedAmount;
        vestingToken.transfer(msg.sender, unreleasedAmount);
    }
    
    function getVestedAmount(address account) external view returns (uint256) {
        uint256 totalVestingTime = block.timestamp - startTime;
        uint256 vestedAmount = (vestingBalances[account] * totalVestingTime) / 1 years;
        return vestedAmount;
    }
    
    function getUnreleasedAmount(address account) external view returns (uint256) {
        uint256 vestedAmount = getVestedAmount(account);
        uint256 unreleasedAmount = vestedAmount - releasedBalances[account];
        return unreleasedAmount;
    }
}
