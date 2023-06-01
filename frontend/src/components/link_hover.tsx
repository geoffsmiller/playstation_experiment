import { css } from '@emotion/react'

const LinkHover = css`
    @media not all and (hover: none) {
        :hover {
            text-decoration: underline;
        }
    }
`

export default LinkHover
