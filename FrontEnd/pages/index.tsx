import { useWeb3React } from "@web3-react/core";
import Head from "next/head";
import Link from "next/link";
import { useEffect, useState } from "react";
import Account from "../components/Account";
import NativeCurrencyBalance from "../components/NativeCurrencyBalance";
import TokenBalance from "../components/TokenBalance";
import { ALBT_TOKEN_ADDRESS, US_ELECTION_ADDRESS } from "../constants";
import useEagerConnect from "../hooks/useEagerConnect";

function Home() {
  const { account, library } = useWeb3React();

  const triedToEagerConnect = useEagerConnect();
  
  const changePage = () => {
    window.location.href = "/main.tsx";
  };

  const isConnected = typeof account === "string" && !!library;
  
  useEffect(() => {
    if (isConnected) {
      changePage();
    }
  }, [isConnected]);

  return (
    <div>
      <Head>
        <title>BreachSneach</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <header>
        <nav>
          <button className="hustle-button">BreachSneach</button>
          <button className="hustle-button-empty">AAAA</button>
          <button className="hustle-button">About us</button>
          <button className="hustle-button-empty">AAAA</button>
          <button className="hustle-button">Why AI?</button>
          <button className="hustle-button-empty">AAAA</button>
          <button className="hustle-button">Stay Informed</button>
          <button className="hustle-button-empty">AAAA</button>
          <button className="hustle-button">Donate</button>
        </nav>
      </header>

      <main>
        <h1 className="text">Welcome to BreachSneach</h1>

        <h2 className="small-text"> The Decentrilized AI-Based Crypto Aattack Predicition Solution  
        <h5>To get started authenticate using you crypto wallet</h5>
        </h2>

        <Account triedToEagerConnect={triedToEagerConnect} />
          
        <h2 className="small-text"> sahdhwjdsakfhfwqjkdhsajkfh
          sadjkwqjdhkasjdfhfw asd wqdas fwa
        </h2>

        
        <h2 className="small-text"> sahdhwjdsakfhfwqjkdhsajkfh
          sadjkwqjdhkasjdfhfw asd wqdas fwa
        </h2>

        <Link className="" href="/">
            <img height="217" width="283" src="https://raw.githubusercontent.com/TariCAD-sistema/BreachSneach/main/logo.png"/>
          </Link>

          {/* --- show user balance  */}
          {/* // <section>
          //   <NativeCurrencyBalance />

          //   <TokenBalance tokenAddress={ALBT_TOKEN_ADDRESS} symbol="ALBT" />
          //   <USLibrary contractAddress={US_ELECTION_ADDRESS} />
          // </section> */} 
      </main>

      <style jsx>{`
        nav {
          display: flex;
          padding: 16px;
          justify-content: space-between;
          align-items: center;
          background-color: black;

          // display: flex;
          // justify-content: space-between;
        }

        main {
          padding: 16px;
          text-align: center;
          background-image: url('https://raw.githubusercontent.com/TariCAD-sistema/BreachSneach/hustle/FrontEnd/images/bg1-gc-bl.jpeg');
        }
        
        .text {
          color: white;
        }

        .small-text {
          font-weight: 400;
          color: white;
          background-color: black;
        }

        .hustle-button {
          padding: .75rem 1.25rem;
          // font-family: "Sono";
          font-size: large; 
          background-color: black;
          color: white;
          font-weight: 700;
          text-transform: uppercase;
          // border-radius: 0.5rem;
          border-color: white;
          border-width: medium;
        }

        .hustle-button-empty {
          padding: .75rem 1.25rem;
          // font-family: "Sono";
          font-size: large; 
          background-color: black;
          color: black;
          font-weight: 700;
          text-transform: uppercase;
          // border-radius: 0.5rem;
          border-color: black;
          border-width: medium;
        }
      `}</style>
    </div>
  );
}

export default Home;
