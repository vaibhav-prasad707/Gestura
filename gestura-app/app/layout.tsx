import "./globals.css"
import type { Metadata } from "next"
import { Inter } from "next/font/google"
import type React from "react" // Added import for React

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "Gestura - Accessible Voice Assistant",
  description:
    "Voice-controlled assistant for blind and deaf users, featuring task management, video calls, and chat functionality.",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <body className={`${inter.className} bg-gradient-to-b from-slate-900 to-purple-900 text-white min-h-screen`}>
        {children}
      </body>
    </html>
  )
}

