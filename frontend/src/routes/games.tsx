import { faLink } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import * as React from 'react';
import { useLoaderData, Link } from 'react-router-dom';
import Card from '../components/card'
import CardsContainer from '../components/cards_container';
import GameTable from '../components/game_table';
import InternalLink from '../components/internal_link';

export async function gamesLoader() {
    const games = await fetch(`${process.env.REACT_APP_API_URL}/games/games/`);
    return games.json();
}

export default function Games() {
    const response = useLoaderData() as any;
    return (
        <div>
            <CardsContainer>
                <Card>
                    <h2>Games List</h2>
                    <GameTable>
                        {response.results.map((game: any) => (
                            <tr>
                                <td><InternalLink to={`/games/${game.id}`}><FontAwesomeIcon icon={faLink} /> {game.name}</InternalLink></td>
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
