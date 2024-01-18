import { Text, useBreakpointValue } from '@chakra-ui/react'

function Title() {
  const fontSize = useBreakpointValue({ base: '4xl', md: '6xl' })

  return (
    <Text
      bgGradient='linear(to-l, #7928CA, #FF0080)'
      bgClip='text'
      fontSize={fontSize}
      fontWeight='extrabold'
    >
      City Pop Generator
    </Text>
  )
}

export default Title;