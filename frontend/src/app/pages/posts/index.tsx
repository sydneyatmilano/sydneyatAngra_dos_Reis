import Layout from "@/app/components/Layout";

export default function PostList() {
    return (
        <Layout>
            <div className="container mx=auto py-10 px-4">
                <h1 className="text-3xl font-bold mb-6">Blog Posts</h1>
                <p className="text-lg">No posts yet. Stay tuned!</p>
            </div>
        </Layout>
    );
}