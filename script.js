const cornAddress = "0xa0c45509036c422ea7c4d4fcac26a9925531d8c3"
const popCornAddress = "0x6531547b44784dDD8A934fB9fEB92ba582dfeD15"
const popCornMachine = "0x1193d3f5d97e9a8a3B4511a718Eda88C21722B44"
async function setup() {
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    const provider = new ethers.providers.Web3Provider(window.ethereum)

    const signer = provider.getSigner()

    const corn = new ethers.Contract(
        cornAddress,
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
    return { signer, corn, bet }
}

async function connect(){
    await window.ethereum.request({ method: 'eth_requestAccounts' });
}

async function approve() {
    const { corn } = await setup()
    try {
        await corn.approve(popCornMachine, "8000000000000000000000")
    } catch (e) { alert(e) }
}

async function enterBet() {
    const { bet } = await setup()
    try {
        await bet.betUsdc()
    } catch (e) { alert(e) }
}
