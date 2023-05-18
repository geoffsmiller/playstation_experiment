import styled from '@emotion/styled'

const CardsContainer = styled.div`
    margin: 2vh auto;
    padding: 0 2vw;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    width: 95vw;

    h3, p {
        text-shadow: 1px 1px 1px #858484;
        color: #1c1c1c;
        margin: 1vh 0 .5vh 0;
    }

    h3 {
        font-size: 2.5vh;

        @media (max-width: 1024px) {
            font-size: 2.25vh
        }
        @media (max-width: 768px) {
            font-size: 2.25vh;
        }
        @media (max-width: 425px) {
            font-size: 2vh;
        }
    }

    p {
        font-size: 2vh;

        @media (max-width: 1024px) {
            font-size: 1.75vh
        }
        @media (max-width: 768px) {
            font-size: 1.75vh;
        }
        @media (max-width: 425px) {
            font-size: 1.75vh;
        }
    }
`

export default CardsContainer
