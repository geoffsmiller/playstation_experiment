import React from "react";
import ReactDOM from "react-dom/client";
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import Layout from "./routes/layout";
import Episodes, { episodesLoader } from './routes/episodes'
import Games, { gamesLoader } from './routes/games'
import Index, { seriesLoader } from './routes/index'
import Episode, { episodeLoader } from "./routes/episode";
import './index.css'

const router = createBrowserRouter([
    {
        path: "/",
        element: <Layout />,
        loader: episodesLoader,
        children: [
            {
                index: true,
                element: <Index />,
                loader: seriesLoader
            },
            {
                path: "/episodes/",
                element: <Episodes />,
                loader: episodesLoader
            },
            {
                path: "/episodes/:episodeId/",
                element: <Episode />,
                loader: episodeLoader
            },
            {
                path: "/games/",
                element: <Games />,
                loader: gamesLoader
            }
        ]
    },
]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>
);
