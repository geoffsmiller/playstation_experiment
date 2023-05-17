import * as React from 'react';
import { useLoaderData } from 'react-router-dom';

export async function episodesLoader() {
    const episodes = await fetch("http://localhost:8000/episodes/episodes/");
    return episodes.json();
}

export default function Episodes() {
    const response = useLoaderData() as any;
    console.log(response)
    return (<div>Episodes {response.count}</div>)
}
