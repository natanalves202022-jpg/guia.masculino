import math,wave,random,json,subprocess
from pathlib import Path
sr=22050
data=json.load(open('src/timing.json'));duration=sum(x['frames'] for x in data)/30
random.seed(4);buf=bytearray();starts=[];at=0
for x in data:starts.append(at);at+=x['frames']/30
for i in range(int(sr*duration)):
 t=i/sr;s=sum(.025*math.sin(2*math.pi*f*t) for f in [110,164.81,220,261.63]);beat=t%.625
 s+=.15*math.sin(2*math.pi*(57*beat+3*(1-math.exp(-beat*35))))*math.exp(-beat*24)
 for a in starts:
  z=t-a
  if 0<=z<.38:s+=.045*random.uniform(-1,1)*math.sin(math.pi*z/.38)**2
 s*=min(1,t/.5)*min(1,(duration-t)/1.5)
 buf.extend(int(max(-1,min(1,s))*32767).to_bytes(2,'little',signed=True))
with wave.open('public/soundtrack.wav','wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(buf)
subprocess.run(['ffmpeg','-v','error','-y','-i','public/soundtrack.wav','-b:a','96k','public/soundtrack.mp3'],check=True)
