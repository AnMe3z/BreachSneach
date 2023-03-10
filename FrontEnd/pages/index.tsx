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
          <Link href="/">
            <img height="217" width="283" src="https://raw.githubusercontent.com/TariCAD-sistema/BreachSneach/main/logo.jpg"/>
          </Link>
        </nav>
      </header>

      <main>
        <h1>Welcome to BreachSneach</h1>

        <h2> sahdhwjdsakfhfwqjkdhsajkfh
          sadjkwqjdhkasjdfhfw asd wqdas fwa
        </h2>

        <Account triedToEagerConnect={triedToEagerConnect} />

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
          justify-content: space-between;
        }

        main {
          text-align: center;
        }
      `}</style>
    </div>
  );
}

export default Home;
