const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export async function analyzeMessage(message) {
  const response = await fetch(`${API_URL}/api/analyze`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  })

  if (!response.ok) {
    const body = await response.json().catch(() => ({}))
    throw new Error(body.detail?.[0]?.msg || body.detail || 'The message could not be analyzed.')
  }

  return response.json()
}