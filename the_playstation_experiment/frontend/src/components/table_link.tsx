import styled from '@emotion/styled'
import { Link } from 'react-router-dom'
import LinkHover from './link_hover'

const TableLink = styled(Link)`
    color: #1c1c1c;
    text-decoration: none;
    ${LinkHover}
`
export default TableLink
