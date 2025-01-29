import Link from "next/link";

export default function Header() {
    return (
        <header className="bg-gray-800 text-white py-4">
            <div className="container mx-auto flex justify-between items-center px-4">
                <h1 className="text-2xl font-bold">My Blog</h1>
                <nav>
                    <ul className="flex space-x-6">
                        <li>
                            <Link href="/" className="hover:underline">Home</Link>
                        </li>
                        <li>
                            <Link href="/posts" className="hover:underline">Posts</Link>
                        </li>
                        <li>
                            <Link href="/login" className="hover:underline">Login</Link>
                        </li>
                    </ul>
                </nav>
            </div>
        </header>
    );
}
