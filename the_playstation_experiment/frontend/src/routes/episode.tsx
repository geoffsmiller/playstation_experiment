import * as React from 'react';
import { useLoaderData } from 'react-router-dom';
import Card from '../components/card';
import CardsContainer from '../components/cards_container';

export async function episodeLoader({ params }: any) {
    const episode = await fetch(`http://localhost:8000/episodes/episodes/${params.episodeId}`);
    return episode.json();
}

export default function Episode() {
    const response = useLoaderData() as any
    return (
        <CardsContainer>
            <Card>
                <h2>{response.series.name} | {response.name}</h2>
                <h3>Release date: {response.release_date}</h3>
                <h3>Coverage date span: {response.coverage_date_span}</h3>
                <p>{response.description}</p>
                <p><a href={`${response.youtube_link}`}>Watch episode on YouTube.</a></p>
                <p><a href={`${response.supplemental_playlist}`}>YouTube supplemental material playlist.</a></p>
                <h3>Segments</h3>
                {response.segments.map((segment: any) => (
                    <div>
                        <h4>{segment.short_title}</h4>
                        <h5><a href={`${segment.youtube_link}`}>Start time: {segment.start_time}</a></h5>
                        <h5>Sources</h5>
                        {segment.sources.map((source: any) => (
                            <p><a href={`${source.link}`}>{source.description}</a></p>
                        ))}
                    </div>
                ))}
            </Card>
        </CardsContainer >
    )
}
