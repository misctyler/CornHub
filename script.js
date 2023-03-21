const cornAddress = "0xa0c45509036c422ea7c4d4fcac26a9925531d8c3"
const popCornAddress = "0x6531547b44784dDD8A934fB9fEB92ba582dfeD15"
const popCornMachine = "0x1193d3f5d97e9a8a3B4511a718Eda88C21722B44"


async function setup() {
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    const provider = new ethers.providers.Web3Provider(window.ethereum)

    const abi = require('./ABI_corn.json'); 
    const contract = new ethers.Contract(cornAddress, abi, provider);
    
    const signer = provider.getSigner()
    async function getBalance() {
        const connectedAccount = await signer.getAddress();
        const balance = await contract.balanceOf(connectedAccount);
        document.getElementById("balance").textContent = ethers.utils.formatUnits(balance, 18);
      }
      getBalance();

    const corn = new ethers.Contract(
        cornAddress,
        [
            "function approve(address, uint) external",
        ],
        signer
    )
    const popcorn = new ethers.Contract(
        popCornAddress,
        [
            "function approve(address, uint) external",
        ],
        signer
    )
    const poppin = new ethers.Contract(
        popCornMachine,
        [
            "function burnKernel(uint) external",
        ],
        signer
    )
    const minty = new ethers.Contract(
        popCornMachine,
        [
            "function mint(uint) external",
        ],
        signer
    )
    return { signer, corn, popcorn, poppin, minty }
}

async function connect(){
    await window.ethereum.request({ method: 'eth_requestAccounts' });
}

async function approve() {
    const { corn } = await setup()
    try {
        await corn.approve(popCornMachine, "100000000000000000000000")
    } catch (e) { alert(e) }
}

async function approve2() {
    const { popcorn } = await setup()
    try {
        await popcorn.approve(popCornMachine, "100000000000000000000000")
    } catch (e) { alert(e) }
}

async function burncorn(_amt) {
    const { poppin } = await setup()
    try {
        await poppin.burnKernel(_amt)
    } catch (e) { alert(e) }
}

async function mintnft(_amt) {
    const { minty } = await setup()
    try { 
        await minty.mint(_amt)
    } catch (e) { alert(e) }
}
