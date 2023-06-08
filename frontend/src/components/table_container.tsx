import styled from '@emotion/styled'
import LinkHover from './link_hover'

const TableContainer = styled.table`
    margin: 1vh 0 1vh 0;
    border: 3px solid #1f1f1f;
    width: 100%;
    text-align: center;
    border-collapse: collapse;

    td, th {
        border: 1px solid #1f1f1f;
        padding: .1vw .125vw;
        font-size: 1.5vw;
    
        @media (max-width: 1024px) {
            font-size: 1.75vw;
        }
        @media (max-width: 768px) {
            font-size: 2.25vw;
        }
        @media (max-width: 425px) {
            font-size: 2.5vw;
        }
        @media (max-width: 320px) {
            font-size: 2.75vw;
        }
    }

    tr:nth-child(even) {
        background: #e5e5e5;
    }

    tr:nth-child(odd) {
        background: #bbbbbb;
    }

    thead th {
        background: #1f1f1f;
        font-weight: bold;
        color: #e5e5e5;
        text-align: center;
        border-left: 2px solid #000000;
        border-bottom: 2px solid #000000;
    }
`

export default TableContainer
