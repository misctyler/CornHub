// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract VestingContract is Ownable {
    
    using SafeMath for uint256;
    address public tokenAddress;
    address public vestingTokenAddress;
    uint256 public totalAmount;
    uint256 public vestingDuration;
    uint256 public vestingStartTime;
    uint256 public totalVested;
    mapping (address => VestingSchedule[]) public vestingSchedules;
    struct VestingSchedule {
        uint256 amount;
        uint256 releaseTime;
    }

    event Vested(address indexed beneficiary, uint256 amount);
    constructor(
        address _tokenAddress,
        address _vestingTokenAddress,
        uint256 _totalAmount,
        uint256 _vestingDuration,
        uint256 _vestingStartTime
    ) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_vestingTokenAddress != address(0), "Vesting token address cannot be zero");
        require(_totalAmount > 0, "Total amount cannot be zero");
        require(_vestingDuration > 0, "Vesting duration cannot be zero");
        tokenAddress = _tokenAddress;
        vestingTokenAddress = _vestingTokenAddress;
        totalAmount = _totalAmount;
        vestingDuration = _vestingDuration;
        vestingStartTime = _vestingStartTime;
    }

    function addVestingSchedule(address beneficiary, uint256 amount) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary address cannot be zero");
        require(amount > 0, "Amount cannot be zero");
        require(totalVested.add(amount) <= totalAmount, "Total vested amount cannot exceed total amount");
        uint256 releaseTime = vestingStartTime.add(vestingDuration);
        vestingSchedules[beneficiary].push(VestingSchedule(amount, releaseTime));
        totalVested = totalVested.add(amount);
        IERC20(vestingTokenAddress).transferFrom(msg.sender, address(this), amount);
    }

    function releaseVestedTokens() external {
        VestingSchedule[] storage schedules = vestingSchedules[msg.sender];
        uint256 totalReleased = 0;
        for (uint256 i = 0; i < schedules.length; i++) {
            VestingSchedule storage schedule = schedules[i];
            if (schedule.releaseTime <= block.timestamp) {
                uint256 amount = schedule.amount;
                schedule.amount = 0;
                totalReleased = totalReleased.add(amount);
                emit Vested(msg.sender, amount);
            }
        }

        if (totalReleased > 0) {
            IERC20(tokenAddress).transfer(msg.sender, totalReleased);
        }
    }
}
