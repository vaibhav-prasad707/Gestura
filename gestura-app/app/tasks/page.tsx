"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Mic, Plus } from "lucide-react"

interface Task {
  id: number
  content: string
  completed: boolean
}

export default function TasksPage() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [isListening, setIsListening] = useState(false)

  const addTask = (content: string) => {
    setTasks([
      ...tasks,
      {
        id: Date.now(),
        content,
        completed: false,
      },
    ])
  }

  const toggleTask = (id: number) => {
    setTasks(tasks.map((task) => (task.id === id ? { ...task, completed: !task.completed } : task)))
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Voice-Controlled Tasks</h1>

      <div className="mb-8 flex gap-4">
        <Button
          onClick={() => setIsListening(!isListening)}
          className={isListening ? "bg-red-500 hover:bg-red-600" : ""}
        >
          <Mic className="mr-2 h-5 w-5" />
          {isListening ? "Listening..." : "Add Task by Voice"}
        </Button>
        <Button variant="outline">
          <Plus className="mr-2 h-5 w-5" />
          Add Task Manually
        </Button>
      </div>

      <div className="space-y-4">
        {tasks.map((task) => (
          <div key={task.id} className="flex items-center gap-4 p-4 bg-white/5 rounded-lg">
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => toggleTask(task.id)}
              className="h-5 w-5 rounded border-gray-300"
            />
            <span className={task.completed ? "line-through text-gray-400" : ""}>{task.content}</span>
          </div>
        ))}
      </div>

      {tasks.length === 0 && (
        <p className="text-center text-gray-400 mt-8">
          No tasks yet. Start by adding a task using your voice or manually.
        </p>
      )}
    </div>
  )
}

