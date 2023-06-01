import * as React from 'react';
import { useLoaderData } from 'react-router-dom';
import Card from '../components/card'
import CardsContainer from '../components/cards_container';
import EpisodeTable from '../components/episode_table';
import TableLink from '../components/table_link';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faLink } from '@fortawesome/free-solid-svg-icons';


export async function episodesLoader() {
    const episodes = await fetch("http://localhost:8000/episodes/episodes/");
    return episodes.json();
}

export default function Episodes() {
    const response = useLoaderData() as any;
    return (
        <CardsContainer>
            <Card>
                <h2>Episodes List</h2>
                <EpisodeTable>
                    {response.results.map((episode: any) => (
                        <tr>
                            <td><TableLink to={`/episodes/${episode.id}`}><FontAwesomeIcon icon={faLink} /> {episode.name}</TableLink></td>
                            <td>{episode.series.name}</td>
                            <td>{episode.coverage_date_span_string}</td>
                            <td>{episode.release_date_string}</td>
                        </tr>
                    ))}
                </EpisodeTable>
            </Card>
        </CardsContainer>
    )
}
