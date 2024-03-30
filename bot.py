# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
import os
import requests
import config

from discord.ext import commands
from bs4 import BeautifulSoup


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=">>", intents=intents)

st_accept = "text/html"
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
headers = {"Accept": st_accept, "User-Agent": st_useragent}


@bot.event
async def on_ready():

    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.command()
async def stat(ctx, profile_name: str, profile_id: str):
    try:
        if profile_name == "aisuru":
            await ctx.send(
                "Бля, твою стату было настолько больно считать, что я аж заплакал"
            )
        req = requests.get(
            f"https://tracker.gg/valorant/profile/riot/{profile_name}%23{profile_id}/overview",
            headers=headers,
        )
        src = req.text

        soup = BeautifulSoup(src, "html.parser")
        statistics_line = soup.find("div", {"class": "giant-stats"})
        all_statistics = statistics_line.find_all("div", {"class": "numbers"})
        player = {
            "Damage/Round": "",
            "K/D Ratio": "",
            "Headshot %": "",
            "Win %": "",
        }
        for statistics in all_statistics:
            name = statistics.find("span", {"class": "name"}).text
            player[name] = statistics.find("span", {"class": "value"}).text

        message = f"Статистика по {profile_name}:\n-----------------------------------------\nDamage/Round: {player['Damage/Round']} | K/D Ratio: {player['K/D Ratio']} | Headshot %: {player['Headshot %']} | Win %: {player['Win %']}"

        await ctx.send(message)
    except Exception as e:
        await ctx.send("https://tenor.com/view/imba3-gif-25714137")


@bot.command()
async def xyesos(ctx, member: discord.Member, times: int):
    try:
        if times > 10:
            await ctx.send(
                "https://tenor.com/view/%D1%82%D1%8B%D1%87%D1%82%D0%BE%D0%B4%D0%B5%D0%B1%D0%B8%D0%BB-%D0%B0%D0%BD%D1%82%D0%BE%D0%BD%D0%BB%D0%B0%D0%B2%D0%BB%D0%B0%D0%B7%D0%B0%D1%80%D0%B5%D0%B2-%D1%82%D1%8B%D0%B4%D1%83%D1%80%D0%B0%D0%BA-%D1%82%D1%8B%D0%B8%D0%B4%D0%B8%D0%BE%D1%82-%D1%82%D1%8B%D1%82%D1%83%D0%BF%D0%BE%D0%B9-gif-16514995"
            )
        else:
            for i in range(times):
                await ctx.send(f"{member.mention} ты реально хуесос")
    except Exception as e:
        await ctx.send("https://tenor.com/view/imba3-gif-25714137")
        print(e)


if __name__ == "__main__":
    bot.run(token=config.BOT_TOKEN)
