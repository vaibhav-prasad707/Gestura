import { Button } from "@/components/ui/button"

export default function CTA() {
  return (
    <section className="py-20" aria-labelledby="cta-heading">
      <div className="container mx-auto px-4 text-center">
        <h2
          id="cta-heading"
          className="text-3xl sm:text-4xl font-bold mb-6 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent"
        >
          Start Using Gestura Today
        </h2>
        <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
          Join thousands of users who are already experiencing the power of voice-controlled accessibility.
        </p>
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <Button size="lg">Get Started for Free</Button>
          <Button variant="outline" size="lg">
            Schedule Demo
          </Button>
        </div>
      </div>
    </section>
  )
}

