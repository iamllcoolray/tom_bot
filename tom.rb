require 'discordrb'
require 'dotenv'

Dotenv.load

bot = Discordrb::Bot.new(
    token: ENV['DISCORD_TOKEN'],
    client_id: ENV['DISCORD_CLIENT_ID'],
    intents: [:server_messages]
)

bot.message do |event|
    next if event.user.bot_account?
    event.respond "Hi there! I heard you."
end

bot.ready do
    puts "Bot is online as #{bot.profile.username}"
end

bot.run
