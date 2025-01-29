// 클라이언트에서 API 호출 (React 컴포넌트)

'use client';

import useSWR from 'swr';

const fetcher = (url: string) => fetch(url).then((res) => res.json());

export default function PostsPage() {
    const { data, error } = useSWR('/api/posts', fetcher);

    if (error) return <div>Failed to load posts</div>;
    if (!data) return <div>loading...</div>;

    return (
        <div>
            <h1 className="text-2xl font-bold mb-4">Posts</h1>
            <ul>
                {data.map((post: { id: number; title: string; content: string }) => (
                    <li key={post.id} className="border-b py-2">
                        <h2 className="text-xl font-semibold">{post.title}</h2>
                        <p>{post.content}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}