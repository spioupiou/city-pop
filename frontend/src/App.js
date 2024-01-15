import { ChakraProvider, Text, Container } from '@chakra-ui/react'
import GenerateButton from './components/GenerateButton';

function App() {
  return (
    <ChakraProvider>
      <Container>
        <Text
          bgGradient='linear(to-l, #7928CA, #FF0080)'
          bgClip='text'
          fontSize='6xl'
          fontWeight='extrabold'
        >
          City Pop Generator
        </Text>
        <GenerateButton/>
      </Container>
    </ChakraProvider>
  );
}

export default App;
