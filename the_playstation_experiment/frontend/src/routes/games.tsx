import * as React from 'react';
import { useLoaderData } from 'react-router-dom';
import Card from '../components/card'

export async function gamesLoader() {
    const games = await fetch("http://localhost:8000/games/games/");
    return games.json();
}

export default function Games() {
    const response = useLoaderData() as any;
    return (
        <div>
            <h1>Search</h1>
            <h1>Games</h1>
            {response.results.map((result: any) => (
                <Card>
                    <ul>
                        <li>{result.name}</li>
                    </ul>
                </Card>
            ))}
        </div>
    )
}
