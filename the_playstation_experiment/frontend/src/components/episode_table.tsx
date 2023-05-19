import * as React from 'react'
import TableContainer from './table_container'

type EpisodeTableProps = {
    children?: React.ReactNode
}

const EpisodeTable = ({ children }: EpisodeTableProps) => {
    return (
        <TableContainer>
            <thead>
                <th>Episode Name</th>
                <th>Series</th>
                <th>Coverage Date Span</th>
                <th>Release Date</th>
            </thead>
            {children}
        </TableContainer>
    )
}

export default EpisodeTable
