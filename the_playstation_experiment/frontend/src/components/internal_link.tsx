import styled from "@emotion/styled";
import LinkHover from "./link_hover";
import { Link } from "react-router-dom";

const InternalLink = styled(Link)`
    text-decoration: none;
    ${LinkHover}
`

export default InternalLink
