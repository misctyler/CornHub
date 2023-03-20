const cornAddress    = "0xa0c45509036c422ea7c4d4fcac26a9925531d8c3"
const popCornAddress = "0x6531547b44784dDD8A934fB9fEB92ba582dfeD15"
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

    const popCorn = new ethers.Contract(
        popCornAddress,
        [
           "function approve(address, uint) external",
        ],
        signer
    )

    const cornBurn = new ethers.Contract(
        popCornMachine,
        [
            "function burnKernel(uint) external",
        ],
        signer
    )

    const NFTburn = new ethers.Contract(
        popCornMachine,
	[
	   "function mint(uint) external",
	],
	signer
    )

    return { signer, corn, cornBurn }
}

async function connect(){
    await window.ethereum.request({ method: 'eth_requestAccounts' });
}

async function approveCorn() {
    const { corn } = await setup()
    try {
        await corn.approve(popCornMachine, "80000000000000000000000")
    } catch (e) { alert(e) }
}

async function burnCorn() {
    const { cornBurn } = await setup()
    //const _amount = document.GetElementById("corn-burn").value
    try {
        await cornBurn.burnKernel( )
    } catch (e) { alert(e) }
}

async function approvePopCorn() {
    const { popCorn } = await setup()
    try {
        await popCorn.approve(popCornMachine, "80000000000000000000000")
    } catch (e) { alert(e) }
}

async function mintNFT() {
    const { NFTburn } = await setup()
    //const __amount = document.GetElementByID("popcorn-burn").value
    try {
        await NFTburn.mint( )
    } catch (e) { alert(e) }
}
