import styled from '@emotion/styled';
import { faLink } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import * as React from 'react';
import { useLoaderData } from 'react-router-dom';
import Card from '../components/card';
import CardsContainer from '../components/cards_container';
import ExternalLink from '../components/external_link';
import InternalLink from '../components/internal_link';
import MissingCoverArt from '../images/missing_cover_art.png'

export async function gameLoader({ params }: any) {
    const game = await fetch(`${process.env.REACT_APP_API_URL}/games/games/${params.gameId}`);
    return game.json();
}

const GameHeaderGrid = styled.div`
    align-items: top;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    margin: .5vh .1vw .5vh .1vw;

    @media (max-width: 768px) {
        grid-template-columns: 1fr;
        grid-template-rows: 2f 1fr;
    }

    p, h3, h4 {
        margin-left: 0;
    }
`
const GameCoverArtDiv = styled.div`
    margin: 0;
    grid-area: 1 / 1 / 2 / 2;
`

const GameCoverArt = styled.img`
    max-width: 25vw;
    max-height: 100vh;

    @media (max-width: 768px) {
        max-width: 90vw;
        max-height: 50vh;
    }
`

const GameInfo = styled.div`
    width: 65vw;
    padding: auto;
    grid-area: 1 / 2 / 2 / 3;

    h2 {
        font-size: 4.5vw;
    }

    a, h3 {
        font-size: 1.5vw;
        margin-top: 1vh;
    }

    @media (max-width: 768px) {
        width: 90vw;
        grid-area: 2 / 1 / 3 / 2;

        h2 {
            font-size: 6vw;
        }

        a, h3 {
            font-size: 3vw;
        }
    }
`

const GameReleaseGrid = styled.div`
    align-items: center;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    border: 2px solid #1c1c1c;
    border-radius: 8px;
    margin: .1vw;
    background-color: #edecec;

    p, h3, h4 {
        margin-left: 0;
    }
`

const GameReleaseCoverArtDiv = styled.div`
    margin: auto;
    padding: .1vw;
    grid-area: 1 / 1 / 2 / 2;
`

const GameReleaseCoverArt = styled.img`
    max-width: 25vw;
    max-height: 30vh;
`
const GameReleaseInfo = styled.div`
    width: 62vw;
    padding: auto;
    grid-area: 1 / 2 / 2 / 3;

    h3 {
        font-size: 2vw;
    }

    a, h4 {
        font-size: 1vw;
        margin: .125vw;
    }

    @media (max-width: 768px) {
        h3 {
            font-size: 4vw;
        }

        a, h4 {
            font-size: 2vw;
        }
    }
`

const RegionFlagImg = styled.img`
    max-width: 1.75vw;
    border: 1px solid #1f1f1f;

    @media (max-width: 1024px) {
        max-width: 2vw;
    }
    @media (max-width: 768px) {
        max-width: 2.75vw;
    }
    @media (max-width: 425) {
        max-width: 3vw;
    }
`

export default function Game() {
    const game = useLoaderData() as any
    return (
        <CardsContainer>
            <Card>
                <GameHeaderGrid>
                    <GameCoverArtDiv><GameCoverArt src={(game.cover_art) ? game.cover_art : MissingCoverArt} /></GameCoverArtDiv>
                    <GameInfo>
                        <h2>{game.name}</h2>
                        <h3>Release date: {game.release_date}</h3>
                        <h3>Developers: {game.developers}</h3>
                        <h3>Publishers: {game.publishers}</h3>
                        <h3>Episode: <InternalLink to={`/episodes/${game.segment.episode.id}`}><FontAwesomeIcon icon={faLink} /> {game.segment.episode.series.name} | {game.segment.episode.name}</InternalLink></h3>
                        <h3>Segment: {game.segment.short_title}</h3>
                        {(game.cover_art) ? <h3>Cover art source: <ExternalLink href={game.cover_art_source_link} target="_blank"><FontAwesomeIcon icon={faLink} /> {game.cover_art_source_name}</ExternalLink></h3> : ''}
                    </GameInfo>
                </GameHeaderGrid>
            </Card>
            <Card>
                <h2>Releases</h2>
                {game.releases.map((release: any) => (
                    <GameReleaseGrid>
                        <GameReleaseCoverArtDiv><GameReleaseCoverArt src={(release.cover_art) ? release.cover_art : MissingCoverArt} /></GameReleaseCoverArtDiv>
                        <GameReleaseInfo>
                            <h3>{release.name}</h3>
                            <h4>Release date: {release.release_date_string}</h4>
                            <h4>Region: <RegionFlagImg src={release.region.flag} alt={release.region.name} title={release.region.name} /></h4>
                            <h4>Platform: {release.platform.name}</h4>
                            <h4>Serial number: {release.serial_number}</h4>
                            <h4>Publisher: {release.publisher.name}</h4>
                            {(release.cover_art) ? <h4>Cover art source: <ExternalLink href={release.cover_art_source_link} target="_blank"><FontAwesomeIcon icon={faLink} /> {release.cover_art_source_name}</ExternalLink></h4> : ''}
                        </GameReleaseInfo>
                    </GameReleaseGrid>
                ))}
            </Card>
        </CardsContainer >
    )
}
