import * as React from 'react'
import styled from '@emotion/styled'
import { useLoaderData, Link, Outlet } from 'react-router-dom'
import CardsContainer from '../components/cards_container';
import Card from '../components/card'
import RedLetter from '../components/red_letter'

export async function seriesLoader() {
    const episodes = await fetch("http://localhost:8000/episodes/series/");
    return episodes.json();
}

const SeriesGrid = styled.div`
    align-items: center;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
`

const LogoImageDiv = styled.div`
    grid-area: 1 / 1 / 2 / 2;
`

const LogoImage = styled.img`
    width: 25vw;
    height: auto;

    @media (max-width: 768px) {
        width: 35vw;
    }
    @media (max-width: 425px) {
        width: 30vw;
    }
`

const SeriesInfo = styled.div`
    width: 65vw;
    grid-area: 1 / 2 / 2 / 3;

    @media (max-width: 768px) {
        width: 55vw;
    }
`

export default function Index() {
    const response = useLoaderData() as any;
    return (
        <div>
            <h2>THE PLAYSTATION <RedLetter>E</RedLetter>XPERIMENT is a chronogaming project with the aim to exhaustively cover every game for fifth generation video game consoles.</h2>
            <h3>The full family of chronogaming series comprises the titular flagship series as well as companion series covering the Sony PlayStation's two major competitors, the Sega Saturn and Nintendo 64, along with minor competitors such as the 3DO Interactive Multiplayer and NEC PC-FX.</h3>
            <h3>This companion website is an episode guide to the series. You can find links to original sources as well as find information about the games covered on the series.</h3>
            <CardsContainer>
                {response.results.map((result: any) => (
                    <Card>
                        <SeriesGrid>
                            <LogoImageDiv><LogoImage src={result.logo} /></LogoImageDiv>
                            <SeriesInfo>
                                <h3>{result.name}</h3>
                                <p>{result.description}</p>
                            </SeriesInfo>
                        </SeriesGrid>
                    </Card>
                ))}
            </CardsContainer>
        </div>
    );
}
