import * as React from 'react';
import { useLoaderData, Link } from 'react-router-dom';
import Card from '../components/card'
import CardsContainer from '../components/cards_container';
import EpisodeTable from '../components/episode_table';

export async function episodesLoader() {
    const episodes = await fetch("http://localhost:8000/episodes/episodes/");
    return episodes.json();
}

export default function Episodes() {
    const response = useLoaderData() as any;
    return (
        <div>
            <CardsContainer>
                <h2>Episodes List</h2>
                <Card>
                    <EpisodeTable>
                        {response.results.map((episode: any) => (
                            <tr>
                                <td><Link to={`/episodes/${episode.id}`}>{episode.name}</Link></td>
                                <td>{episode.series.name}</td>
                                <td>{episode.coverage_date_span}</td>
                                <td>{episode.release_date}</td>
                            </tr>
                        ))}
                    </EpisodeTable>
                </Card>
            </CardsContainer>
        </div >
    )
}
