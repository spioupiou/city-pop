import { ChakraProvider, Center, Box, VStack, Flex } from '@chakra-ui/react'
import GenerateButton from './components/GenerateButton';
import Title from './components/Title';


function App() {
  return (
  <ChakraProvider>
    <Flex justifyContent="center" alignItems="center" height="100vh" p={4}>
      <Box border="1px" borderColor="teal.500" p={6} shadow="lg" bgColor="white">
        <Center>
          <VStack spacing={6}>
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
