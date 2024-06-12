import emoji

print("Emojis disponíveis:\n❤️ - :red_heart:\n👍 - :thumbs_up:\n🤔 - :thinking_face:\n🥳 - :partying_face:")

r = input("Digite uma frase e ela será emojizada: ")
frase = emoji.emojize(r)

print("Frase emojizada:", frase)