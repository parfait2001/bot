from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

bot = Bot(token='6044726081:AAGWttb8bVFTaL_zvwIaRV9jNvi83Po3AA0')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="👋 S'inscrire maintenant", callback_data="register")
button2 = InlineKeyboardButton(text="👉🏼 Comment s'inscrire ?", callback_data="helper")
button3 = InlineKeyboardButton(text="💋 Envoyer une capture", callback_data="capt")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)
keyboard_inline1 = InlineKeyboardMarkup().add(button1)
keyboard_inline2 = InlineKeyboardMarkup().add(button2,button3)
keyboard_inline3 = InlineKeyboardMarkup().add(button3)


keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("✅ Demmarer","👋 S'inscrire maintenant", "💋 Groupe télégram","👉🏼 Comment s'inscrire ?")

keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("✅ Demmarer","👋 S'inscrire maintenant", "💋 Groupe télégram","👉🏼 Comment s'inscrire ?")


keyboard5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("👋 S'inscrire maintenant").add("👉🏼 Comment s'inscrire ?")


@dp.message_handler(commands=['random'])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)



@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("1xBET_OFFICIEL\n\n Offre exclusive ! 100$ offerts gratuitement 😲😲 Avec le code promo 1XBet.\n\nCréez un nouveau compte 1xbet avec le code promo 👇🏼 TOM21 👉🏼 \n\nAvec le code promo TOM21, vous serez éligible à plusieurs offres sur 1xbet : 100$ offerts gratuitement lors de l'inscription avec le code promo TOM21\n\n200% de bonus sur votre premier dépôt jusqu'à 300$ \n\nRecevez jusqu'à 25% de remboursement si vous perdez de l'argent avec le code promo TOM21.\n\nNe ratez pas cette expérience ! Inscrivez-vous avec le CODE PROMO TOM21 et ne manquez aucune de nos offres.\n\n1xbet officiel est disponible dans tous les pays du monde 🥳🥳.\n\nLien : https://ln.run/z-mqU", reply_markup=keyboard_inline)

@dp.callback_query_handler(text=["register", "helper","capt"])
async def random_value(call: types.CallbackQuery):
    if call.data == "register":
        await call.message.answer("Lien : https://ln.run/z-mqU\n\n Après avoir terminé votre inscription en utilisant notre code promo \"TOM21\", vous devez nous envoyer une capture d'écran via ce bot afin de recevoir le lien de notre groupe Telegram et accéder aux coupons de pari.\n\n ",reply_markup=keyboard_inline2)
    if call.data == "helper":
        await call.message.answer("🔴 Comment s'inscrire sur 1xbet\n\n👉 Une fois l'application installé choisir toujours l'inscription complète , en un clik ou pas téléphone.\n\n 👉 Comment procéder\n1- Nom \n2- Prénom \n3- Pays\n4- Région\n5- Ville \n6- Date de naissance\n7- Monaie de votre pays\n8- Adresse e-mail\n9- Numéro téléphone\n 10- Mot de passe\n11-  Répété le mot de passe\n12- Code promo 👉 TOM21 👉\n✅ Et en fin coché la case vide et valider l'inscription sur le bouton",reply_markup=keyboard_inline1)
    if call.data == "capt":
        await call.message.answer("Afin d'obtenir le lien vers notre groupe Telegram ainsi que l'accès aux coupons de pari, veuillez envoyer une capture d'écran de l'inscription avec le code promo \"TOM21\" via ce bot.")
        @dp.message_handler(content_types=types.ContentTypes.PHOTO)
        async def random_answers(message: types.Message):
            await message.reply("https://t.me/+JxW4wxqaOG0wZTc0")

    await call.answer()


@dp.message_handler()
async def kb_answer(message: types.Message):

    if message.text == "👋 S'inscrire maintenant":
        await message.reply("Lien : https://ln.run/z-mqU\n\n Après avoir terminé votre inscription en utilisant notre code promo \"TOM21\", vous devez nous envoyer une capture d'écran via ce bot afin de recevoir le lien de notre groupe Telegram et accéder aux coupons de pari.\n\n ")
        #await call.answer("💋 Groupe télégram")
    elif message.text == '💋 Groupe télégram':
        await message.reply("https://t.me/+JxW4wxqaOG0wZTc0")
    elif message.text == "👉🏼 Comment s'inscrire ?":
        await message.reply("🔴 Comment s'inscrire sur 1xbet\n\n👉 Une fois l'application installé choisir toujours l'inscription complète , en un clik ou pas téléphone.\n\n 👉 Comment procéder\n1- Nom \n2- Prénom \n3- Pays\n4- Région\n5- ville \n6- date de naissance\n7- monaie de votre pays\n8- adresse e-mail\n9- numéro téléphone\n 10- mot de passe\n11-  Répété le mot de passe\n12- Code promo 👉 TOM21 👉\n✅ Et en fin coché la case vide et valider l'inscription sur le bouton")
        await message.answer_photo("https://github.com/parfait2001/Projet-Flutter/blob/main/WhatsApp%20Image%202023-04-08%20at%2010.03.50.jpeg?raw=true")
    elif message.text == "✅ Demmarer":
        await message.reply(f"Bienvenue dans ce bot qui vous offre des coupons gagnants 1xbet tous les jours, ainsi que des prévisions de scores exacts illimités.\n\n Pour profiter de ces services, veuillez d'abord vous inscrire sur 1xbet avec le code promo TOM21.\n Si vous ne savez pas comment vous inscrire, vous pouvez cliquer sur comment s'inscrire.\n Sinon, vous pouvez cliquer sur s'inscrire maintenant.\n\nJe vous souhaite bonne chance et n'hésitez pas à me contacter si vous avez des questions ou des préoccupations.")
    else:
        await message.reply(f"{message.text} ✅")


executor.start_polling(dp)