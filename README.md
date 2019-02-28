# 디스코드 뮤직봇

Subject : Music Bot

Date : 2019 - 01 - 28 <br>
Launge : Python <br>
Sample : Discord Develpor, Youtbe 섹시베이비, YouTube Lucas <br>
Site : https://discordpy.readthedocs.io/en/latest/api.html#discord.VoiceClient.create_ytdl_player
       https://www.youtube.com/channel/UCR-zOCvDCayyYy1flR5qaAg/videos
       https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php
       https://gracefullight.github.io/2018/03/26/download-music-video-with-youtube-dl/

확인해야할것
1. youtube_dl -> cmd -> python -m pip install -U youtube_dl

Update : 2019 - 01- 30
Now command 
  - ~명령어 : 사용할 수 있는 명령어 확인
  - ~입장 : 음악 봇을 사용자가 있는 음성채널로 입장
  - ~나가 : 음성채널에서 강퇴
  - ~play \<Link\> : Youtube 주소를 가져와 바로 재생 
  - ~pause : 재생중인 음악 일시정지
  - ~stop : 재생중인 음악 종료
  - ~선택 <A, B, C> : 선택하기 어려울때 사용

2019-02-25 : 에러 발생
Error Code : Error in the pull function.
             Read error
             The specified session has been invalidated for some reason.
             
Answer : 5초에 한번씩 Url 다시 받아오기 해결 및 Download로 해결완료             
             
2019-02-28 : Error 해결 완료
