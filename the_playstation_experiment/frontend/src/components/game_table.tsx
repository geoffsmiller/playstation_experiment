import * as React from 'react'
import TableContainer from './table_container'

type GameTableProps = {
    children?: React.ReactNode
}

const GameTable = ({ children }: GameTableProps) => {
    return (
        <TableContainer>
            <thead>
                <th>Name</th>
                <th>Release Date</th>
                <th>Platforms</th>
                <th>Developers</th>
                <th>Publishers</th>
            </thead>
            {children}
        </TableContainer>
    )
}

export default GameTable
