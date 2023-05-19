import styled from '@emotion/styled';
import * as React from 'react';
import { useLoaderData } from 'react-router-dom';
import Card from '../components/card';
import CardsContainer from '../components/cards_container';

export async function gameLoader({ params }: any) {
    const game = await fetch(`http://localhost:8000/games/games/${params.gameId}`);
    return game.json();
}

const GameHeaderGrid = styled.div`
    align-items: top;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;

    @media (max-width: 768px) {
        grid-template-columns: 1fr;
        grid-template-rows: 2f 1fr;
    }

    p, h3, h4 {
        margin-left: 0;
    }
`
const GameCoverArtDiv = styled.div`
    margin: 5px;
    grid-area: 1 / 1 / 2 / 2;
`

const GameCoverArt = styled.img`
    max-width: 45vw;
    max-height: 100vh;

    @media (max-width: 768px) {
        max-width: 90vw;
        max-height: 50vh;
    }
`

const GameInfo = styled.div`
    width: 45vw;
    padding: auto;
    grid-area: 1 / 2 / 2 / 3;

    @media (max-width: 768px) {
        width: 90vw;
        grid-area: 2 / 1 / 3 / 2;
    }
`

export default function Game() {
    const response = useLoaderData() as any
    return (
        <CardsContainer>
            <Card>
                <GameHeaderGrid>
                    <GameCoverArtDiv><GameCoverArt src={response.cover_art} /></GameCoverArtDiv>
                    <GameInfo>
                        <h2>{response.name}</h2>
                        <h4>Release date: {response.release_date}</h4>
                        <h4>Developers: {response.developers}</h4>
                        <h4>Publishers: {response.publishers}</h4>
                        <h4>Segment: {response.segment.title}</h4>
                        <h3>Releases</h3>
                    </GameInfo>
                </GameHeaderGrid>

            </Card>
        </CardsContainer >
    )
}
