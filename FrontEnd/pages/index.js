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
          src="https://raw.githubusercontent.com/AnMe3z/BreachSneach/main/FrontEnd/pages/images/Logo.jpg"
          boxSize="300px"
        />
      </ChakraProvider>
    );
  }
}
