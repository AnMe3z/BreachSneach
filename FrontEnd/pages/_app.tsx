import { Web3ReactProvider } from "@web3-react/core";
import type { AppProps } from "next/app";
import getLibrary from "../getLibrary";
import "../styles/globals.css";
import { Sono } from '@next/font/google'

const roboto = Sono({
  subsets: ['latin'],
  weight: '400',
})

function NextWeb3App({ Component, pageProps }: AppProps) {
  return (
    <main className={roboto.className}>
      <Web3ReactProvider getLibrary={getLibrary}>
        <Component {...pageProps} />
      </Web3ReactProvider>
    </main>
  );
}

export default NextWeb3App;
