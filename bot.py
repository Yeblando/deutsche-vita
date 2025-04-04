{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0  import telegram\
from telegram.ext import Updater, CommandHandler\
\
# \uc0\u1042 \u1072 \u1096  \u1090 \u1086 \u1082 \u1077 \u1085 \
TOKEN = '7916092260:AAEKZ3jEiC5_bwCuUO8AHpiEOdZQ-K6IL1k'\
\
# \uc0\u1060 \u1091 \u1085 \u1082 \u1094 \u1080 \u1103  \u1086 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1082 \u1080  \u1082 \u1086 \u1084 \u1072 \u1085 \u1076 \u1099  /start\
def start(update, context):\
    update.message.reply_text("\uc0\u1055 \u1088 \u1080 \u1074 \u1077 \u1090 , \u1084 \u1080 \u1088 !")\
\
# \uc0\u1057 \u1086 \u1079 \u1076 \u1072 \u1077 \u1084  Updater \u1080  \u1087 \u1077 \u1088 \u1077 \u1076 \u1072 \u1077 \u1084  \u1077 \u1084 \u1091  \u1090 \u1086 \u1082 \u1077 \u1085 \
updater = Updater(TOKEN, use_context=True)\
dispatcher = updater.dispatcher\
\
# \uc0\u1044 \u1086 \u1073 \u1072 \u1074 \u1083 \u1103 \u1077 \u1084  \u1086 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1095 \u1080 \u1082  \u1082 \u1086 \u1084 \u1072 \u1085 \u1076 \u1099  /start\
dispatcher.add_handler(CommandHandler("start", start))\
\
# \uc0\u1047 \u1072 \u1087 \u1091 \u1089 \u1082  \u1073 \u1086 \u1090 \u1072 \
updater.start_polling()\
updater.idle()\
}