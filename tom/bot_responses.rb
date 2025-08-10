require 'dotenv'
require 'openai'

Dotenv.load

client = OpenAI::Client.new(access_token: ENV['OPENAI_API_KEY'])

response = client.chat.completions.create(
    model: "gpt-4.1-nano",
    messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "Hello, how do I use OpenAI with Ruby?" }
    ]
    temperature: 0.7,
    max_tokens: 500,
)

puts response.dig("choices", 0, "message", "content")