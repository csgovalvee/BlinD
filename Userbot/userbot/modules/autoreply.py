import asyncio

from userbot.events import register

message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Risponderò il prima possibile.\n\nðﾟﾑﾉðﾟﾏﾻ NON spammatemi troppi messaggi, Quando torno ONLINE mi dici quello di cui hai bisogno.**"
exempt = []
mutedList = []
autoNiceText = False

@register(outgoing=True, pattern="^.pula$")
async def CARABINIERIIIIIIIIIII(e):
  for i in range(10):
    await asyncio.wait([e.edit("🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴")])
    await asyncio.sleep(0.1)
  await asyncio.wait([e.edit("**ARRIVA DANILO IL FALLITO!**")])

@register(outgoing=True, pattern="^.ficca$")
async def ficca(e):
  for i in range(5):
    await asyncio.wait([e.edit("👉🏻👌🏻 OHH")])
    await asyncio.sleep(0.2)
    await asyncio.wait([e.edit("👉🏻 👌🏻OHH SII ")])
    await asyncio.sleep(0.2)
    await asyncio.wait([e.edit("👉🏻  👌🏻OOOOOOH ")])
    await asyncio.sleep(0.2)
  await asyncio.wait([e.edit("OHH SIII!")])

@register(outgoing=True, pattern="^Addy$")
async def Addy(e):
	await asyncio.wait([e.edit("__1SaMuUFiPC3LnRUh4nqZ67dGUQc12wFAT__")])

@register(outgoing=True, pattern="^.fv$")
async def fv(e):
	await asyncio.wait([e.edit("massimofrattarelli@yahoo.it")])

@register(outgoing=True, pattern="^TC$")
async def TC(e):
	await asyncio.wait([e.edit("Trisomico Cerebroleso con la 104")])

@register(outgoing=True, pattern="^lcl$")
async def lcl(e):
	await asyncio.wait([e.edit("lavati con l'acido e fatti qualche shottino di cloroformio,retard del cazzo")])

@register(outgoing=True, pattern="^MAM$")
async def MAM(e):
	await asyncio.wait([e.edit("ma ammazzati coglione faccia di merda")])

@register(outgoing=True, pattern="^.shop$")
async def shop(e):
	await asyncio.wait([e.edit("SamuShop.atshop.io")])

@register(outgoing=True, pattern="^.comandi$")
async def comandi(e):
	await asyncio.wait([e.edit(".pula\nAddy\n.fv\nTC\nlcl\nMAM\n.shop\n.ficca\n.cgb\n.channels\n.LOSER")])

@register(outgoing=True, pattern="^.cgb$")
async def Scam(e):
	await asyncio.wait([e.edit("List of chargebackers:\n@ChargeBackList\n@ChargeBackers")])

@register(outgoing=True, pattern="^.channels$")
async def Channels(e):
	await asyncio.wait([e.edit("List of my channels/groups:\n@SamuOGMarket\n@SamuOGChannels\n@SamuChat\n@CompraVenditaItaly")])

@register(outgoing=True, pattern="^.LOSER$")
async def LOSER(e):
	await asyncio.wait([e.edit("@N3rdyi is a fucking kid and loser")])

@register(outgoing=True)
async def niceText(e):
  if e.text[0].isalpha() and not e.text == "Canali":
    global autoNiceText
    if autoNiceText:
      mex = ""
      for i in range(len(e.text)):
        if e.text[i] == " ":
          mex = mex + ' '
        else:
          mex = mex + e.text[i]
        await asyncio.wait([e.edit("`" + mex + " |`")])
        await asyncio.sleep(0.1)
        await asyncio.wait([e.edit("`" + mex + "  ‏‏‎ `")])
        await asyncio.sleep(0.1)
        if i == len(e.text) - 1:
          await asyncio.wait([e.edit("`" + e.text + "`")])

@register(outgoing=True, pattern="^.niceText$")
async def setNiceText(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global autoNiceText
    if autoNiceText:
      autoNiceText = False
      await e.edit("`Animazione Testo Disattivata!`")
    else:
      autoNiceText = True
      await e.edit("`Animazione Testo Attivata!`")

@register(outgoing=True, pattern="^.mex")
async def setMessage(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global message
    message = str(e.text[5:])
    await e.edit("`Messaggio impostato correttamente!`")

@register(outgoing=True, pattern="^.mute$")
async def setMute(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    if e.is_private and not (await e.get_sender()).bot:
      global mutedList
      if e.chat_id in mutedList:
        mutedList.remove(e.chat_id)
        await e.edit("`Utente Smutato!`")
      else:
        mutedList.append(e.chat_id)
        await e.edit("`Utente Mutato!`")

@register(incoming=True)
async def autoReply(e):
  if e.is_private and not (await e.get_sender()).bot:
    global mutedList
    if e.chat_id in mutedList:
      await e.delete()
    else:
      if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
        global exempt
        if not e.sender.id in exempt:
          exempt.append(e.sender.id)
          x = 0
          while True:
            if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
              await asyncio.sleep(1)
              x += 1
              if x >= 1:
                global message
                await e.respond(message)
                exempt.remove(e.sender.id)
                break
            else:
              exempt.remove(e.sender.id)
              break
