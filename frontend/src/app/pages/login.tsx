import Layout from "../components/Layout";

export default function Login() {
    return (
        <Layout>
            <div className="container mx-auto py-10 px-4">
                <h1 className="text-3xl font-bold mb-6">Login</h1>
                <form className="max-w-md mx-auto bg-gray-100 p-6 rounded shadow">
                    <div className="mb-4">
                        <label htmlFor="email" className="block text-sm font-medium text-gray-700">Email</label>
                        <input
                            type="email"
                            id="email"
                            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounder shadow-sm focus:outline-none focus:ring-indigo-200"
                            placeholder="Enter your email"
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="password" className="block text-sm font-medium text-gray-700">Password</label>
                        <input
                            type="password"
                            id="password"
                            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-indigo-200"
                            placeholder="Enter your password"
                        />
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-indigo-600 text-white py-2 px-4 rounded hover:bg-indigo-700"
                    >
                        Login
                    </button>
                </form>
            </div>
        </Layout>
    );
}