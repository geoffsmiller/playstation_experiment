import styled from '@emotion/styled'
import LinkHover from './link_hover'

const CardsContainer = styled.div`
    margin: 2vh auto;
    padding: 0 2vw;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    width: 95vw;
    height: fit-content;
 
    h2, h3, h4, p, a {
        text-shadow: 1px 1px 1px #858484;
        color: #1c1c1c;
        margin: 1vh 0 .5vh 0;
    }

    h2 {
        font-size: 2.25vw;

        @media (max-width: 1024px) {
            font-size: 2.25vw;
        }
        @media (max-width: 768px) {
            font-size: 3vh;
        }
        @media (max-width: 425px) {
            font-size: 3vh;
        }
    }

    h3 {
        font-size: 1.75vw;
        margin: 2px;

        @media (max-width: 1024px) {
            font-size: 1.75vw
        }
        @media (max-width: 768px) {
            font-size: 2.5vw;
        }
        @media (max-width: 425px) {
            font-size: 2.5vw;
        }
    }

    h4 {
        font-size: 1.5vw;
        margin-left: .5vw;

        @media (max-width: 768px) {
            font-size: 2vw;
        }
    }

    ul {
        list-style: none;
        padding-inline-start: 2.5vw;
    }

    p, a, li {
        font-size: 1.25vw;

        @media (max-width: 1024px) {
            font-size: 1.25vw;
        }
        @media (max-width: 768px) {
            font-size: 2vw;
        }
        @media (max-width: 425px) {
            font-size: 2vw;
        }
    }
`

export default CardsContainer
