require 'dotenv'
require 'openai'

Dotenv.load

client = OpenAI::Client.new(access_token: ENV['OPENAI_API_KEY'])

system_prompt = File.read("prompt.txt").strip

conversation = [
    { role: "system", content: system_prompt },
    { role: "assistant", content: "What's up?" }
]

def openai_response(conversation)
    response = client.chat.completions.create(
        model: "gpt-4.1-nano",
        messages: conversation
        temperature: 0.7,
        max_tokens: 500,
    )

    return response
end

def get_bot_response(user_message)
    user_message.downcase
    user_message = user_message.sub("/tom", "")

    conversation.push({"role": "user", "content": user_message})

    response = openai_response(conversation)

    oai_reply = response.dig("choices", 0, "message", "content")

    return oai_reply
end