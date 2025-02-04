import { Button } from "@/components/ui/button"

export default function VideoDemo() {
  return (
    <section className="py-20 bg-slate-900/50" aria-labelledby="video-demo-heading">
      <div className="container mx-auto px-4">
        <div className="grid md:grid-cols-2 gap-12 items-center">
          <div>
            <h2
              id="video-demo-heading"
              className="text-3xl font-bold mb-6 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent"
            >
              Accessible Video Conferencing
            </h2>
            <p className="text-gray-300 mb-6">
              Experience video calls with real-time captions, sign language interpretation, and voice commands. Perfect
              for both blind and deaf users.
            </p>
            <ul className="space-y-4 mb-8">
              <li className="flex items-center text-gray-300">
                <span className="mr-2 text-purple-400">•</span>
                Real-time speech-to-text captions
              </li>
              <li className="flex items-center text-gray-300">
                <span className="mr-2 text-purple-400">•</span>
                Sign language interpreter support
              </li>
              <li className="flex items-center text-gray-300">
                <span className="mr-2 text-purple-400">•</span>
                Voice-controlled interface
              </li>
            </ul>
            <Button size="lg">Try Video Call</Button>
          </div>
          <div className="relative aspect-video rounded-lg overflow-hidden bg-slate-800">
            <div className="absolute inset-0 flex items-center justify-center">
              <p className="text-gray-400">Video Demo Placeholder</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

