export const metadata = {
  title: "My Blog",
  description: "A simple blog platform",
};

export default function RootLayout({ children }: { children: React.ReactNode}) {
  return (
    <html lang="ko">
      <body className="bg-gray-50 text-gray-900">
        {children}
      </body>
    </html>
  );
}