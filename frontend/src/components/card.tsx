import * as React from 'react'
import styled from '@emotion/styled'

type CardProps = {
    children?: React.ReactNode
}

const CardContainer = styled.div`
    background-color: #bbbbbb;
    block-size: fit-content;
    width: 95vw;
    padding: 0 .5vw;
    border: 2px solid #1f1f1f;
    border-radius: 8px;
    margin: .2vw;
    opacity: 90%;
`

const Card = ({ children }: CardProps) => {
    return (
        <CardContainer>
            {children}
        </CardContainer>
    )
}

export default Card
