import * as React from 'react';
import { useLoaderData, Link } from 'react-router-dom';
import Card from '../components/card'
import CardsContainer from '../components/cards_container';
import GameTable from '../components/game_table';

export async function gamesLoader() {
    const games = await fetch("http://localhost:8000/games/games/");
    return games.json();
}

export default function Games() {
    const response = useLoaderData() as any;
    return (
        <div>
            <CardsContainer>
                <h2>Games List</h2>
                <Card>
                    <GameTable>
                        {response.results.map((game: any) => (
                            <tr>
                                <td><Link to={`/games/${game.id}`}>{game.name}</Link></td>
                                <td>{game.release_date}</td>
                                <td>{game.platforms}</td>
                                <td>{game.developers}</td>
                                <td>{game.publishers}</td>
                            </tr>
                        ))}
                    </GameTable>
                </Card>
            </CardsContainer>
        </div>
    )
}
