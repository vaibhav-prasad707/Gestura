"use client"

import { Button } from "@/components/ui/button"
import { Mic } from "lucide-react"
import { useState, useEffect } from "react"

export default function Hero() {
  const [isListening, setIsListening] = useState(false)
  const [transcript, setTranscript] = useState("")

  // Initialize speech recognition
  useEffect(() => {
    if (typeof window !== "undefined") {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
      if (SpeechRecognition) {
        const recognition = new SpeechRecognition()
        recognition.continuous = true
        recognition.interimResults = true

        recognition.onresult = (event) => {
          const last = event.results.length - 1
          setTranscript(event.results[last][0].transcript)
        }

        if (isListening) {
          recognition.start()
        }

        return () => {
          recognition.stop()
        }
      }
    }
  }, [isListening])

  return (
    <section className="relative overflow-hidden py-20 sm:py-32">
      <div className="container mx-auto px-4">
        <div className="max-w-3xl mx-auto text-center">
          <h1 className="text-4xl sm:text-5xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
            Your Voice-Powered Digital Assistant
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            Control your digital world effortlessly with voice commands. Perfect for everyone, especially designed for
            blind and deaf users.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Button
              size="lg"
              className="group relative"
              onClick={() => setIsListening(!isListening)}
              aria-pressed={isListening}
            >
              <Mic className={`mr-2 h-5 w-5 ${isListening ? "text-red-400" : ""}`} />
              {isListening ? "Listening..." : "Start Voice Command"}
            </Button>
            <Button variant="outline" size="lg">
              Watch Tutorial
            </Button>
          </div>
          {transcript && (
            <div className="mt-8 p-4 bg-white/10 rounded-lg">
              <p className="text-gray-300">Heard: {transcript}</p>
            </div>
          )}
        </div>
      </div>
      <div
        className="absolute inset-0 -z-10"
        style={{
          backgroundImage: `url(${process.env.NEXT_PUBLIC_VERCEL_URL}/gradient-bg.svg)`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          opacity: 0.2,
        }}
        aria-hidden="true"
      />
    </section>
  )
}

