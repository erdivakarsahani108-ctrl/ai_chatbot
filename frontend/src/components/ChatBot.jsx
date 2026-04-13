import { useState } from 'react'

function ChatBot({ apiUrl }) {
  const [query, setQuery] = useState('')
  const [chat, setChat] = useState([
    { who: 'bot', text: 'Ask anything about your grievance and I will help route it.' },
  ])
  const [status, setStatus] = useState('Ready to chat')

  const sendMessage = async () => {
    if (!query.trim()) return
    const userMessage = { who: 'user', text: query }
    setChat((prev) => [...prev, userMessage])
    setStatus('Waiting for AI response...')

    const reply = await fetchChatReply(query, apiUrl)
    setChat((prev) => [...prev, { who: 'bot', text: reply }])
    setQuery('')
    setStatus('Ready to chat')
  }

  const fetchChatReply = async (message, apiUrl) => {
    try {
      console.log('Chat API URL:', apiUrl, 'Message:', message)
      const res = await fetch(`${apiUrl}/chat/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      })
      console.log('Chat Response Status:', res.status)
      if (!res.ok) {
        const errorText = await res.text()
        console.error('Chat API Error:', errorText)
        throw new Error(`Chat service error: ${res.status}`)
      }
      const data = await res.json()
      console.log('Chat Reply:', data.reply)
      return data.reply
    } catch (error) {
      console.error('Chat Fetch Error:', error)
      return 'AI service unavailable. Please use the complaint form or try again later.'
    }
  }

  return (
    <div className="chat-window">
      <h3>Smart AI Assistant</h3>
      {chat.map((entry, index) => (
        <div key={index} className={`chat-bubble ${entry.who === 'user' ? 'chat-user' : 'chat-bot'}`}>
          {entry.text}
        </div>
      ))}
      <textarea
        value={query}
        placeholder="Describe your issue. Example: 'Paani nahin aa rahi hai'"
        onChange={(e) => setQuery(e.target.value)}
      />
      <button type="button" onClick={sendMessage}>Send</button>
      <p className="load-bar">{status}</p>
    </div>
  )
}

export default ChatBot
