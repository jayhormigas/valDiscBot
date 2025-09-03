import discord
from discord import app_commands
from discord.ext import commands
import requests
import random
from config import DISCORD_TOKEN, VALORANT_API_KEY

# Character images
character_images = {
    'Brimstone': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/51e62f3c74356a7501d06feba42ac643133257d7-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Phoenix': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/47387e354c34d51b84066bc47af3c5755b92b9c5-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Sage': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/58a180961a14beb631877921e647c233804853c1-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Sova': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/08b3d8822544bd327ebed0768c8b90fcec83d1a5-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Viper': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/152244f121e61ca32bdd2bea9fc5370e315664fb-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Cypher': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/4a648cdbcbbeef137050deefeaf6a1369c606666-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Reyna': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/7cb513c9b3eae3286449776e85753138436d553c-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Killjoy': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/820d36d431fff77b1e1ece39ad6f007746bd31f6-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Breach': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/e435c3378b7999a3338b408dbb5da8ba63f91150-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Omen': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/015a083717e9687de8a741cfceddb836775b5f9f-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Jett': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/d41286dc9017bf79c0b4d907b7a260c27b0adb69-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Raze': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/40b4b242b68afe30d21e7f95bdcacaebca46ea60-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Skye': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/37ea1466beebb54aad4f16efbad184566cb80368-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Yoru': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/05e1a996814dd10d7179efee327d29a7be00e912-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Astra': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/ba51d43803082941b0274b66413b0acc972546dd-616x822.png?auto=format&fit=fill&q=80&w=218',
    'KAY/O': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/fe52e0efac73ec782b19a54e98a4658b03677407-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Chamber': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/0f5b668b77499c0051201389d6ac5e7343c9727f-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Neon': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/14145d7bf9be17afa80c04ee4fbe200076cc1769-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Fade': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/e7099cc13a665ed2b556d514e50984393ed49967-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Harbor': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/1246b5c517f6c8fa660e884a7032c1c54994003e-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Gekko': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/8d88f133f735f6a9077679b1ece754e5624c728e-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Deadlock': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/477284dfe402a85abcf6b07512bcd6f01c8fe60e-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Iso': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/2c35cef9c38283f8478d1e808b1c129f371e50b3-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Clove': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/9f02060077f9d61dbe89555a339e6231006d9b7b-616x822.png?auto=format&fit=fill&q=80&w=218',
    'Vyse': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/370e4b820670ef0bac7e685f6e8c5e64d19f1890-587x900.png?auto=format&fit=fill&q=80&w=218',
    'Tejo': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/3413df9939de606a355c1f88fbfc35f0774c19c9-587x900.jpg?auto=format&fit=fill&q=80&w=425',
    'Waylay': 'https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/11c2b158d932076d3215749a34b7b4209b48ce44-587x900.png?auto=format&fit=fill&q=80&w=425'
}

# Safe fallback if agent not in dictionary
FALLBACK_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

loseMessage = [
    "lost their recent game ;("
]

# Initialize bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("Bot is up and ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="matchlurk", description="Lurk a player's recent Valorant game.")
@app_commands.describe(
    name="CASE SENSITIVE: The player's username.",
    tag="CASE SENSITIVE: The player's tag (Do not include the #)."
)
async def matchlurk(interaction: discord.Interaction, name: str, tag: str):
    await interaction.response.defer()

    region = "na"
    url = f"https://api.henrikdev.xyz/valorant/v3/matches/{region}/{name}/{tag}?api_key={VALORANT_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "data" in data and len(data["data"]) > 0:
        metadata = data["data"][0].get("metadata", {})
        map_name = metadata.get("map", "No map information available")

        players = data["data"][0].get("players", {}).get("all_players", [])
        one_player = next((p for p in players if p.get("name") == name), None)

        if one_player:
            character_name = one_player.get("character", "Unknown")
            character_image_url = character_images.get(character_name, FALLBACK_IMAGE)

            team_name = one_player.get("team", "").lower()
            teams = data["data"][0].get("teams", {})
            team = teams.get(team_name, {})

            # Win/Loss/Draw check
            if team.get("rounds_won", 0) > team.get("rounds_lost", 0):
                embed_color = 0x00FF00
                image_url = "https://i.ytimg.com/vi/IcJyT93oseQ/maxresdefault.jpg"
                game_result = f"{one_player.get('name')} won their recent game :D"
            elif team.get("rounds_won", 0) < team.get("rounds_lost", 0):
                embed_color = 0xFF0000
                image_url = "https://pbs.twimg.com/media/GG9pO5DXsAAiG_k?format=jpg&name=small"
                game_result = f"{one_player.get('name')} " + random.choice(loseMessage)
            else:
                embed_color = 0x000000
                image_url = "https://beebom.com/wp-content/uploads/2023/07/Valorant-Game-Remake-draw.jpg"
                game_result = f"{one_player.get('name')} tied their recent game..."

            # Build embed
            embed = discord.Embed(
                title=f"{one_player.get('name')} #{one_player.get('tag')}'s match",
                color=embed_color
            )
            embed.set_author(name="bot created by lowkey gaming", icon_url="https://static.zerochan.net/Chrollo.Lucilfer.full.3350486.jpg")
            embed.set_thumbnail(url=character_image_url)
            embed.set_image(url=image_url)
            embed.add_field(name="Agent", value=character_name, inline=False)
            embed.add_field(name="Map", value=map_name, inline=True)
            embed.add_field(
                name="K/D/A",
                value=f"{one_player.get('stats', {}).get('kills', 'N/A')}/"
                      f"{one_player.get('stats', {}).get('deaths', 'N/A')}/"
                      f"{one_player.get('stats', {}).get('assists', 'N/A')}",
                inline=True
            )
            embed.add_field(
                name="Score",
                value=f"{team.get('rounds_won', 'N/A')} - {team.get('rounds_lost', 'N/A')}",
                inline=True
            )
            embed.add_field(name="Game Result", value=game_result, inline=False)
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send("Player not found")
    else:
        await interaction.followup.send("No match data found")

bot.run(DISCORD_TOKEN)
