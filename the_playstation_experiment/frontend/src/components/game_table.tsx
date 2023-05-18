import * as React from 'react'
import styled from '@emotion/styled'

type GameTableProps = {
    children?: React.ReactNode
}

const GameTableContainer = styled.table`
    margin: 1vh 0 1vh 0;
    border: 3px solid #1f1f1f;
    width: 100%;
    text-align: center;
    border-collapse: collapse;

    td, th {
        border: 1px solid #1f1f1f;
        padding: 3px 4px;
    }

    tbody td {
        font-size: 13px;
    }

    tr:nth-child(even) {
        background: #e5e5e5;
    }

    thead th {
        font-size: 19px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        border-left: 2px solid #a40808;
    }
`
const GameTable = ({ children }: GameTableProps) => {
    return (
        <GameTableContainer>
            <tr>
                <th>Name</th>
                <th>Release Date</th>
                <th>Platforms</th>
                <th>Developers</th>
                <th>Publishers</th>
            </tr>
            {children}
        </GameTableContainer>
    )
}

export default GameTable
