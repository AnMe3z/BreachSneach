import React, { Component } from "react";
import { ChakraProvider, Flex, Heading, Text, Input, Button, Image, useToast } from "@chakra-ui/react";
import { ethers } from "ethers";

const provider = new ethers.providers.Web3Provider(window.ethereum);

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      address: "",
      balance: "",
      isLoggedIn: false,
    };
  }

  async connect() {
    try {
      await window.ethereum.request({ method: "eth_requestAccounts" });
      const accounts = await provider.listAccounts();
      const address = accounts[0];
      const balance = await provider.getBalance(address);
      this.setState({ address, balance, isLoggedIn: true });
      this.toast({
        title: "Connected",
        description: `Address: ${address}\nBalance: ${ethers.utils.formatEther(balance)}`,
        status: "success",
        duration: 5000,
        isClosable: true,
      });
    } catch (error) {
      this.toast({
        title: "Error",
        description: error.message,
        status: "error",
        duration: 5000,
        isClosable: true,
      });
      console.error(error);
    }
  }

  toast = useToast();

  render() {
    const { address, balance, isLoggedIn } = this.state;
    return (
      <ChakraProvider>
        <Flex h="100vh" alignItems="center" justifyContent="center">
          {isLoggedIn ? (
            <Flex direction="column" alignItems="center" justifyContent="center" py={12}>
              <Image src="/metamask.svg" alt="MetaMask" h={24} mb={4} />
              <Heading mb={4}>Logged in</Heading>
              <Text mb={4}>Address: {address}</Text>
              <Text mb={4}>Balance: {ethers.utils.formatEther(balance)} ETH</Text>
            </Flex>
          ) : (
            <Flex direction="column" alignItems="center" justifyContent="center">
              <Image src="/metamask.svg" alt="MetaMask" h={24} mb={4} />
              <Heading mb={4}>Login with MetaMask</Heading>
              <Button colorScheme="blue" onClick={() => this.connect()}>
                Connect
              </Button>
            </Flex>
          )}
        </Flex>
      </ChakraProvider>
    );
  }
}
