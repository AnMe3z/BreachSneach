import React, { Component } from "react";
import { CacheProvider } from '@chakra-ui/next-js'
import { ChakraProvider, Flex } from "@chakra-ui/react";
import { Image } from "@chakra-ui/react";
import { Button, ButtonGroup } from '@chakra-ui/react'

const regex = new RegExp(/\.\/images\//);

const handleButtonClick = () => {
  window.location.href = "";
};

export default class App extends Component {
  render() {
    return (
      <ChakraProvider>
        <Flex h="100vh" alignItems="center" justifyContent="center">
          <Image 
            src="https://raw.githubusercontent.com/AnMe3z/BreachSneach/main/FrontEnd/pages/images/Logo.jpg"
            boxSize="332px x 217px"
          />
          <Button onClick={handleButtonClick} colorScheme="blackAlpha" variant="outline" color="#FFFFFF" borderColor="#32127A" bg="#000000">Get started</Button>
        </Flex>
      </ChakraProvider>
    );
  }
}
