import * as React from 'react'
import styled from '@emotion/styled'

type EpisodeTableProps = {
    children?: React.ReactNode
}

const EpisodeTableContainer = styled.table`
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

const EpisodeTable = ({ children }: EpisodeTableProps) => {
    return (
        <EpisodeTableContainer>
            <tr>
                <th>Episode Name</th>
                <th>Series</th>
                <th>Coverage Date Span</th>
                <th>Release Date</th>
            </tr>

            {children}
        </EpisodeTableContainer>
    )
}

export default EpisodeTable
