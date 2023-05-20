from aiogram import Bot, Dispatcher, types, executor
import random
import os
from dotenv import load_dotenv
import joblib
import pandas as pd

load_dotenv()
bot_token = os.getenv('token')

bot = Bot(token=bot_token)
dp = Dispatcher(bot)
model = joblib.load("model/best_tpot_model1.joblib")


# Define the /start command handler
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Send a welcome message to the user
    await message.reply(
        "Welcome to the Tennis Match Predictor Bot! To predict the winner of a match, use this bot.\n"
        "You have to send a csv file with such columns\n"
        "Here is the example\n"
    )
    with open('good.csv', 'rb') as csv_file:
        await message.reply_document(csv_file)


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def handle_csv_file(message: types.Message):
    # Check if the message contains a document
    if message.document.mime_type == 'text/csv':
        # Download the document
        file_id = message.document.file_id
        file_path = await bot.get_file(file_id)
        file_data = await bot.download_file(file_path.file_path)

        # Process the CSV file
        df = pd.read_csv(file_data)
        df = df[[col for col in df.columns if col != 'Unnamed: 0']]
        # Do something with the dataframe, such as extracting information or performing analysis

        # Reply with a message
        reply_message = f"CSV file received and processed! Rows: {len(df)}, Columns: {len(df.columns)}"
        # await bot.send_message(chat_id=message.chat.id, text=text)
        res = model.predict(df.convert_dtypes())
        pd.DataFrame(res).to_csv('result.csv')
        with open('result.csv', 'rb') as csv_file:
            await message.reply_document(csv_file)
    else:
        await message.reply("Please upload a CSV file.")


# Create the bot and start the event loop

executor.start_polling(dp)
