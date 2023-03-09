import React, { Component } from "react";
import { CacheProvider } from '@chakra-ui/next-js'
import { ChakraProvider } from "@chakra-ui/react";
import { Image } from "@chakra-ui/react";

const regex = new RegExp(/\.\/images\//);

export default class App extends Component {
  render() {
    return (
      <ChakraProvider>
        <div>Your Next.js App</div>
        <Image src="gibbresh.png" fallbackSrc="../images/Logo.png" />
      </ChakraProvider>
    );
  }
}
