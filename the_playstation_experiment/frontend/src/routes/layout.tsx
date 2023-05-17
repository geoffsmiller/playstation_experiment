import * as React from 'react'
import styled from '@emotion/styled'
import Episodes from './episodes'
import { useLoaderData } from 'react-router-dom'

type LayoutProps = {
    children?: React.ReactNode,
}

const LayoutContainer = styled.div`
    display: flex;
    height: 100vh;
    overflow: hidden;
    background-color: #bbbbbb;
`

const NavContainer = styled.div`
    height: 10vh;
    border-bottom: 2px solid #000;
    display: flex;
    align-items: center;
    top: 0;
    flex-direction: row;
    position: fixed;
    width: 100%;
    background-image: linear-gradient(
        45deg,
        #326db3 0%,
        #00aa93 50%,
        #f2c202 100%
    );
    margin: 0;
    padding:0 2vw;
    z-index: 1;
`

const NavItem = styled.div`
    font-size: 3.66vh;
    font-weight: bold;
    font-family: sans-serif;
    text-shadow: 0 0 10px black;
    flex-grow: 1;

    @media (max-width: 1024px) {
        font-size: 3.15vh;
    }
    @media (max-width: 768px) {
        font-size: 3vh;
    }
    @media (max-width: 425px) {
        font-size: 2vh;
        flex-grow: 1.5;
    }
    @media (max-width: 320px) {
        font-size: 2vh;
    }
`

const NavLink = styled.a`
    color: white;
`

const MainContainer = styled.div`
    display: flex;
    width: 100%;
    margin-top: 10vh;
`

export default function Layout({ children }: LayoutProps) {
    const response = useLoaderData() as any;
    return (
        <LayoutContainer>
            <title>The PlayStation Experiment | Chronogaming the fifth generation of video game consoles</title>
            <NavContainer>
                <NavItem><NavLink>THE PLAYSTATION EXPERIMENT</NavLink></NavItem>
                <NavItem>EPISODES</NavItem>
                <NavItem>GAMES</NavItem>
            </NavContainer>
            <MainContainer>
                {response.results.map((result: any) => (
                    <div>
                        <ul>
                            <li>{result.name}</li>
                            <li>{result.description}</li>
                        </ul>
                    </div>
                ))}
            </MainContainer>
        </LayoutContainer>);
}
