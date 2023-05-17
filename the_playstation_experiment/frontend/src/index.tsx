import React from "react";
import ReactDOM from "react-dom/client";
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import Layout from "./routes/layout";
import Episodes, { episodesLoader } from './routes/episodes'

const router = createBrowserRouter([
    {
        path: "/",
        element: <Layout />,
        loader: episodesLoader,
    },
    {
        path: "episodes/",
        element: <Episodes />,
        loader: episodesLoader,
    }
]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>
);
