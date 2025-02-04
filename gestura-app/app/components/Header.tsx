"use client"

import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Menu, X } from "lucide-react"
import { useState } from "react"

export default function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <header className="bg-slate-900/50 backdrop-blur-md border-b border-slate-800" role="banner">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <Link
            href="/"
            className="text-2xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent"
            aria-label="Gestura Home"
          >
            Gestura
          </Link>

          <Button
            variant="ghost"
            className="md:hidden"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-expanded={isMenuOpen}
            aria-controls="mobile-menu"
            aria-label="Toggle menu"
          >
            {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </Button>

          <nav className="hidden md:block" role="navigation">
            <ul className="flex space-x-8">
              <li>
                <Link href="/tasks" className="text-gray-300 hover:text-white transition-colors">
                  Tasks
                </Link>
              </li>
              <li>
                <Link href="/calls" className="text-gray-300 hover:text-white transition-colors">
                  Video Calls
                </Link>
              </li>
              <li>
                <Link href="/chat" className="text-gray-300 hover:text-white transition-colors">
                  Chat
                </Link>
              </li>
              <li>
                <Button variant="secondary">Start Using Gestura</Button>
              </li>
            </ul>
          </nav>
        </div>

        {/* Mobile menu */}
        <div id="mobile-menu" className={`${isMenuOpen ? "block" : "hidden"} md:hidden mt-4`} role="navigation">
          <ul className="flex flex-col space-y-4">
            <li>
              <Link href="/tasks" className="block text-gray-300 hover:text-white transition-colors">
                Tasks
              </Link>
            </li>
            <li>
              <Link href="/calls" className="block text-gray-300 hover:text-white transition-colors">
                Video Calls
              </Link>
            </li>
            <li>
              <Link href="/chat" className="block text-gray-300 hover:text-white transition-colors">
                Chat
              </Link>
            </li>
            <li>
              <Button variant="secondary" className="w-full">
                Start Using Gestura
              </Button>
            </li>
          </ul>
        </div>
      </div>
    </header>
  )
}

