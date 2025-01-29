import Layout from '../components/Layout';
import React, { useEffect, useState } from 'react';
import apiClient from '../lib/apiClient';
import { Post } from '../types';

const PostsList: React.FC = () => {
    const [posts, setPosts] = useState<Post[]>([]);

    useEffect(() => {
        apiClient.get('/posts')
            .then((response:any) => {
                setPosts(response.data);
            })
            .catch((error:any) => {
                console.error('Error fetching posts: ', error);
            });

    }, []);

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Posts</h1>
            <ul>
                {posts.length > 0 ? (
                    posts.map((post) => (
                        <li key={post.id} className="mb-4">
                            <h2 className="text-xl font-semibold">{post.title}</h2>
                        </li>
                    ))
                ) : (
                    <p>No posts availabe.</p>
                )}
            </ul>
        </div>
    );
};

const Home: React.FC = () => {
    return (
        <Layout>
            <div className="container mx-auto py-10 px-4">
                <h1 className="text-4xl font-bold mb-6">Welcome to My Blog</h1>
                <p className="text-lg">
                    Explore the lastest posts and learn more about interesting topics.
                </p>
                <PostsList />
            </div>
        </Layout>
    );
};

export default Home;