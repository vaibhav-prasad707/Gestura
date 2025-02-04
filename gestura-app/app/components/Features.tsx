import { Mic, Video, MessageSquare, ListTodo } from "lucide-react"

const features = [
  {
    icon: <Mic className="h-8 w-8" />,
    title: "Voice Commands",
    description: "Control everything with simple voice commands. Navigate, create tasks, and communicate effortlessly.",
  },
  {
    icon: <Video className="h-8 w-8" />,
    title: "Accessible Video Calls",
    description: "Make video calls with real-time captions and sign language support.",
  },
  {
    icon: <MessageSquare className="h-8 w-8" />,
    title: "Smart Chat",
    description: "Text-to-speech and speech-to-text conversion for seamless communication.",
  },
  {
    icon: <ListTodo className="h-8 w-8" />,
    title: "Task Management",
    description: "Create and manage tasks using voice commands or keyboard shortcuts.",
  },
]

export default function Features() {
  return (
    <section className="py-20" aria-labelledby="features-heading">
      <div className="container mx-auto px-4">
        <h2
          id="features-heading"
          className="text-3xl font-bold text-center mb-12 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent"
        >
          Empowering Features
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {features.map((feature, index) => (
            <div key={index} className="p-6 rounded-lg bg-white/5 hover:bg-white/10 transition-colors">
              <div className="mb-4 text-purple-400">{feature.icon}</div>
              <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
              <p className="text-gray-300">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

