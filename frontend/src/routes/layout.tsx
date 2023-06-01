import * as React from 'react'
import styled from '@emotion/styled'
import { useLoaderData, Link, Outlet } from 'react-router-dom'
import RedLetter from '../components/red_letter'
import LinkHover from '../components/link_hover'
import InternalLink from '../components/internal_link'

const LayoutContainer = styled.div`
    display: flex;
    height: 100vh;
    overflow: hidden;
    background-color: #e5e5e5;
`

const NavContainer = styled.div`
    height: 10vh;
    border-bottom: 2px solid #000;
    display: flex;
    align-items: center;
    top: 0;
    flex-direction: row;
    position: fixed;
    width: 100vw;
    background: linear-gradient(
        45deg,
        #326db3 0%,
        #00aa93 38%,
        #f2c202 92%
    );
    margin: 0;
    padding:0 2vw;
    z-index: 1;
    div {
        transition: font-size .5s;
    }
`

const NavLogo = styled.div`
    display: inline-block;
    font-size: 2.75vh;
    font-weight: bold;
    font-family: sans-serif;
    text-transform: uppercase;
    text-shadow: 0 0 10px #1f1f1f;
    flex-grow: 1;

    @media (max-width: 1024px) {
        font-size: 2.75vh;
    }
    @media (max-width: 768px) {
        font-size: 2.5vh;
    }
    @media (max-width: 425px) {
        font-size: 2vh;
        flex-grow: 1.5;
    }
    @media (max-width: 320px) {
        font-size: 1.5vh;
    }
    ${LinkHover}
`

const NavItem = styled.div`
    display: inline-block;
    font-size: 5vh;
    font-weight: bold;
    font-family: sans-serif;
    text-shadow: 0 0 10px #1f1f1f;
    flex-grow: 1;

    @media (max-width: 1024px) {
        font-size: 4.5vh;
    }
    @media (max-width: 768px) {
        font-size: 4vh;
    }
    @media (max-width: 425px) {
        font-size: 3.5vh;
        flex-grow: 1.5;
    }
    @media (max-width: 320px) {
        font-size: 2vh;
    }
    ${LinkHover}
`

const NavLink = styled(InternalLink)`
    color: #edecec;
`

const ContentContainer = styled.div`
    display: flex;
    width: 100vw;
    margin-top: 10vh;
    overflow-y: scroll;
    overflow-x: hidden;

    h2, h3 {
        text-shadow: 1px 1px 1px #858484;
        margin: 2vh 1vw;
        color: #1c1c1c;
    }

    h2 {
        font-size: 3.5vh;

        @media (max-width: 1024px) {
            font-size: 3vh
        }
        @media (max-width: 768px) {
            font-size: 2.25vh;
        }
        @media (max-width: 425px) {
            font-size: 2vh;
        }
    }

    h3 {
        font-size: 2.5vh;

        @media (max-width: 1024px) {
            font-size: 2vh
        }
        @media (max-width: 768px) {
            font-size: 1.75vh;
        }
        @media (max-width: 425px) {
            font-size: 1.75vh;
        }
    }
`

export default function Layout() {
    const response = useLoaderData() as any;
    return (
        <LayoutContainer>
            <title>The PlayStation Experiment | Chronogaming the fifth generation of video game consoles</title>
            <NavContainer>
                <NavLogo><NavLink to="/">The<br />PlayStation<br /><RedLetter>E</RedLetter>xperiment</NavLink></NavLogo>
                <NavItem><NavLink to="episodes/">Episodes</NavLink></NavItem>
                <NavItem><NavLink to="games/">Games</NavLink></NavItem>
            </NavContainer>
            <ContentContainer>
                <Outlet />
            </ContentContainer>
        </LayoutContainer>);
}
