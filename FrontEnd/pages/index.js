import React, { Component } from "react";
import { CacheProvider } from '@chakra-ui/next-js'
import { ChakraProvider } from "@chakra-ui/react";
import { Image } from "@chakra-ui/react";

const regex = new RegExp(/\.\/images\//);

export default class App extends Component {
  render() {
    return (
      <ChakraProvider>
        <div>Logo</div>
        <Image 
          src=""
          boxSize="200px"
          objectFit="cover"
        />
      </ChakraProvider>
    );
  }
}
