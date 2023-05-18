import * as React from 'react';
import { useLoaderData } from 'react-router-dom';
import Card from '../components/card';
import CardsContainer from '../components/cards_container';

export async function gameLoader({ params }: any) {
    const game = await fetch(`http://localhost:8000/games/games/${params.gameId}`);
    return game.json();
}

export default function Game() {
    const response = useLoaderData() as any
    return (
        <CardsContainer>
            <Card>
                <h2>{response.name}</h2>
                <h3>Release date: {response.release_date}</h3>
            </Card>
        </CardsContainer >
    )
}
