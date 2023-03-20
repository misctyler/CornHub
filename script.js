const usdcAddress = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
const betAddress = "0xa4bfb9ae4999a97c5f93bEE59E4D126C904989aD"

async function setup() {
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    const provider = new ethers.providers.Web3Provider(window.ethereum)

    const signer = provider.getSigner()

    const usdc = new ethers.Contract(
        usdcAddress,
        [
            "function approve(address, uint) external",
        ],
        signer
    )
    const bet = new ethers.Contract(
        betAddress,
        [
            "function betUsdc() external",
        ],
        signer
    )
    return { signer, usdc, bet }
}

async function connect(){
    await window.ethereum.request({ method: 'eth_requestAccounts' });
}

async function approve() {
    const { usdc } = await setup()
    try {
        await usdc.approve(betAddress, "1000000000000")
    } catch (e) { alert(e) }
}

async function enterBet() {
    const { bet } = await setup()
    try {
        await bet.betUsdc()
    } catch (e) { alert(e) }
}
