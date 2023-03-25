using System;
using System.Numerics;
using System.IO;
using Nethereum.Web3;
using Nethereum.Web3.Accounts;
using Nethereum.Web3.Accounts.Managed;
using Nethereum.Web3.Transactions;
using Nethereum.Contracts;

class Program
{
    static void Main(string[] args)
    {
        var corn_token = "0xa0c45509036c422ea7c4d4fcac26a9925531d8c3";
        var popcorn_token = "0x6531547b44784dDD8A934fB9fEB92ba582dfeD15";
        var butter_token = "0x409e02e728418501720d7b1e5d7328ac461ecaae";
        
        var w3 = new Web3("https://rpc-mainnet.maticvigil.com");
        w3.TransactionManager.DefaultGas = BigInteger.Parse("500000");
        w3.TransactionManager.DefaultGasPrice = BigInteger.Parse("20000000000");

        var geth_poa_middleware = new Nethereum.JsonRpc.Client.Middleware.GethPOAMiddleware();
        w3.Client.OverridingRequestInterceptor = geth_poa_middleware;

        var addresses = new Tuple<string, string>[]
        {
            Tuple.Create("0x9bcD90E35A0fCC6aDA241acaBA9A376368B56dF5", "CornHub"),
            Tuple.Create("0x1193d3f5d97e9a8a3B4511a718Eda88C21722B44", "Factory")
        };

        for (int i = 0; i < addresses.Length; i++)
        {
            var balance_wei = w3.Eth.GetBalance.SendRequestAsync(addresses[i].Item1).Result.Value;
            var balance_matic = Web3.Convert.FromWei(balance_wei);
            Console.WriteLine($"{addresses[i].Item2} has a balance of {balance_matic} MATIC");

            check_erc20_bal(w3, corn_token, "CORN", addresses[i].Item1, addresses[i].Item2);
            check_erc20_bal(w3, popcorn_token, "POPCORN", addresses[i].Item1, addresses[i].Item2);
            check_erc20_bal(w3, butter_token, "BUTTER", addresses[i].Item1, addresses[i].Item2);
        }
    }

    static void check_erc20_bal(Web3 w3, string token_address, string ticker, string account_address, string account_name)
    {
        var abi = File.ReadAllText("/home/tyler/CornHub/scripts/ABI_corn.json");
        var token_contract = new Contract(w3.Eth, abi, token_address);
        var balance_call = token_contract.GetFunction("balanceOf");
        var balance_base_unit = balance_call.CallAsync<BigInteger>(account_address).Result;

        var decimals_call = token_contract.GetFunction("decimals");
        var decimals = decimals_call.CallAsync<int>().Result;

        var balance = (decimal)balance_base_unit / (decimal)Math.Pow(10, decimals);
        Console.WriteLine($"{account_name} has a balance of {balance} {ticker} tokens");
    }
}
