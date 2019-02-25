import youtube_dl
import discord
import asyncio
import random
import ffmpeg
import os
import subprocess

from discord import Embed
from pytube import YouTube

client = discord.Client()
#유튜브용으로 사용하는것
players = {}

@client.event
async def on_ready():
    # 실행시 나오는 말
    print("Start")
    print(client.user.name)
    print(client.user.id)
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

    # 봇의 현재 상태
    await client.change_presence(game=discord.Game(name="Music Bot 실행중", type=1))

@client.event
async def on_message(message):

    # 설명서 ( Help )
    if message.content.startswith("~명령어"):
        channel = message.channel
        embed = discord.Embed(
            description = '사용가능한 명령어 입니다.',
            colour= discord.Color.blue()
        )

        embed.add_field(name='~안녕', value= '~인사 들어오면 인사 박아라', inline=False)
        embed.add_field(name='~선택', value='~선택 A B C 이런식으로 사용가능 [여러개 가능]', inline=False)
        embed.add_field(name='~입장', value='음성채팅에 있어야 사용 가능하며 음성챗 으로 불러오기', inline=False)
        embed.add_field(name='~나가', value='음성채팅에서 내보내기', inline=False)
        embed.set_footer(text= '설명 끝')

        await client.send_message(channel, embed= embed)

    # 첫번째 명령어 인사하기
    if message.content.startswith("~안녕"):
        await client.send_message(message.channel, "안녕하세요 주인님!")

    # 두번째 명령어 선택하기
    if message.content.startswith("~선택"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, "당신이 선택한것은 "+ choiceresult)

    # 세번째 명령어 음성채팅에 입장시키기
    if message.content.startswith("~입장"):
        channel = message.author.voice.voice_channel
        server = message.server
        voice_client = client.voice_client_in(server)
        print(voice_client)
        print("들어옴")
        if voice_client == None:
            await client.send_message(message.channel, '들어왔습니다')
            await client.join_voice_channel(channel)
        else:
            await client.send_message(message.channel, '봇이 이미 들어와있습니다.')

    # 네번째 명령어 음성채팅에 나가기
    if message.content.startswith("~나가"):
        server = message.server
        voice_client = client.voice_client_in(server)
        print(voice_client)
        print("나가기")
        if voice_client == None:
            await client.send_message(message.channel, '봇이 음성채널에 접속하지 않았습니다.')
            pass
        else:
            await client.send_message(message.channel, '나갑니다')
            await voice_client.disconnect()

    #음악전용
    #첫번째 검색
    if message.content.startswith("~play"):
        server = message.server
        voice_client = client.voice_client_in(server)
        msg = message.content.split(" ")
        url = msg[1]
        print(url)
        player = await voice_client.create_ytdl_player(url)
        print(player)
        #재생 음악 설명
        await client.send_message(message.channel, "음악을 재생합니다.")
        players[server.id] = player
        player.start()

    # 사용했으니 오류가 뜬다.
    # ydl_opts = {}
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download([url])

    #두번째 정지
    if message.content.startswith("~pause"):
        await client.send_message(message.channel, "음악을 일시정지합니다.")
        id = message.server.id
        players[id].pause()

    #세번째 다시시작
    if message.content.startswith("~resume"):
        await client.send_message(message.channel, "음악을 다시 재생합니다.")
        id = message.server.id
        players[id].resume()

    #네번쨰 음악 종료
    if message.content.startswith("~stop"):
        await client.send_message(message.channel, "음악을 종료합니다.")
        id = message.server.id
        players[id].stop()

client.run('NTM5MzgxOTkxODI1NDczNTQ2.DzBiOw.skHzixYJy7ZUgk3aTcNX10N5Rxs')
