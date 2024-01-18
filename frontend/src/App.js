import { ChakraProvider, Center, Box, VStack, Flex } from '@chakra-ui/react'
import GenerateButton from './components/GenerateButton';
import Title from './components/Title';


function App() {
  return (
    <ChakraProvider>
      <Flex justifyContent="center" alignItems="center" height="100vh" p={4}>
        <Box border="1px" borderColor="lightgray" p={4}>
          <Center>
          <VStack spacing={4}>
            <Title/>
            <GenerateButton/>
            </VStack>
          </Center>
        </Box>
      </Flex>
    </ChakraProvider>
  );
}

export default App;
