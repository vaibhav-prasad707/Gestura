import Header from "./components/Header"
import Hero from "./components/Hero"
import Features from "./components/Features"
import VideoDemo from "./components/VideoDemo"
import CTA from "./components/CTA"
import Footer from "./components/Footer"

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main id="main-content" className="flex-grow">
        <Hero />
        <Features />
        <VideoDemo />
        <CTA />
      </main>
      <Footer />
    </div>
  )
}

