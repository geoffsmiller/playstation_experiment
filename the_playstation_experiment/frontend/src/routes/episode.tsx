import * as React from 'react';
import { Link, useLoaderData } from 'react-router-dom';
import styled from '@emotion/styled'
import Card from '../components/card';
import CardsContainer from '../components/cards_container';
import ExternalLink from '../components/external_link';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLink } from '@fortawesome/free-solid-svg-icons';
import InternalLink from '../components/internal_link';

export async function episodeLoader({ params }: any) {
    const episode = await fetch(`http://localhost:8000/episodes/episodes/${params.episodeId}`);
    return episode.json();
}

const EpisodeHeaderGrid = styled.div`
    align-items: top;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;

    @media (max-width: 768px) {
        grid-template-columns: 1fr;
        grid-template-rows: 2f 1fr;
    }

    p {
        margin-left: 0;
    }
`

const EpisodeThumbnailDiv = styled.div`
    margin: 5px;
    grid-area: 1 / 1 / 2 / 2;
`

const EpisodeThumbnail = styled.img`
    width: 45vw;

    @media (max-width: 768px) {
        width: 90vw;
    }
`

const EpisodeInfo = styled.div`
    width: 45vw;
    padding: auto;
    grid-area: 1 / 2 / 2 / 3;

    @media (max-width: 768px) {
        width: 90vw;
        grid-area: 2 / 1 / 3 / 2;
    }
`

export default function Episode() {
    const response = useLoaderData() as any
    return (
        <CardsContainer>
            <Card>
                <EpisodeHeaderGrid>
                    <EpisodeThumbnailDiv><EpisodeThumbnail src={response.thumbnail_image} /></EpisodeThumbnailDiv>
                    <EpisodeInfo>
                        <h2>{response.series.name} | {response.name}</h2>
                        <h3>Release date: {response.release_date_string}</h3>
                        <h3>Coverage date span: {response.coverage_date_span_string}</h3>
                        <p>{response.description}</p>
                        <p><ExternalLink href={`${response.youtube_link}`} target="_blank"><FontAwesomeIcon icon={faLink} /> Watch episode on YouTube.</ExternalLink></p>
                        <p><ExternalLink href={`${response.supplemental_playlist_link}`} target="_blank"><FontAwesomeIcon icon={faLink} /> YouTube supplemental material playlist.</ExternalLink></p>
                    </EpisodeInfo>
                </EpisodeHeaderGrid>
            </Card >
            <Card>
                <h2>Segments</h2>
                {response.segments.map((segment: any) => (
                    <div>
                        <h3>{segment.short_title} (<ExternalLink href={`${segment.youtube_link}`} target="_blank"><FontAwesomeIcon icon={faLink} /> {segment.start_time})</ExternalLink></h3>
                        {(segment.description) ? (
                            <>
                                <h4>Description</h4>
                                <p>{segment.description}</p>
                            </>
                        ) : ''}
                        {(segment.segment_type == "Release Roundup" && segment.games.length) ? (
                            <>
                                <h4>Featured games</h4>
                                <ul>
                                    {segment.games.map((game: any) => (
                                        <li><InternalLink to={`/games/${game.id}`}><FontAwesomeIcon icon={faLink} /> {game.name}</InternalLink></li>
                                    ))}
                                </ul>
                            </>
                        ) : ''}
                        <h4>Sources</h4>
                        <ul>
                            {segment.sources.map((source: any) => (
                                <li><ExternalLink href={`${source.link}`} target="__blank"><FontAwesomeIcon icon={faLink} /> {source.description}</ExternalLink></li>
                            ))}
                        </ul>

                    </div>
                ))}
            </Card>
        </CardsContainer >
    )
}
