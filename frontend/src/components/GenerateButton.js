import { useState } from 'react';
import { Button, Stack } from '@chakra-ui/react'

const GenerateButton = () => {
  const [data, setData] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleClick = async () => {
    setIsLoading(true);
    
    try {
      const response = await fetch((process.env.REACT_APP_API_URL || 'http://localhost:8000') + '/api/v1');

      const result = await response.json();
      setData(result);
    
    } catch (err) {
      throw Error(`Could not fetch the data - Status Error: ${err.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  console.log(data);

  return ( 
    <Stack direction='column' spacing={4}>
      {data && data.lyrics.map((sentence, index) => (
        <div key={index}>{sentence}</div>
      ))}
      <Button
        onClick={handleClick}
        isLoading={isLoading}
        loadingText='Generating...'
        colorScheme='teal'
        variant='outline'
      >
        Generate
      </Button>
    </Stack>
  )
}

export default GenerateButton;