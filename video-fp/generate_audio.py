import asyncio, json, math, subprocess
from pathlib import Path
import edge_tts
ROOT=Path(__file__).parent
SCRIPTS=[
'Você passa horas vendo vídeos de outras pessoas. E se começasse a criar os seus?',
'Uma página sem aparecer coloca o assunto no centro. Pode ser games, curiosidades ou receitas. Escolha um tema para começar.',
'Depois, transforme uma dúvida em um vídeo útil. Escreva um roteiro simples. Use materiais que você pode usar e faça sua própria edição.',
'Publique, observe o que prende a atenção e melhore o próximo vídeo. A rotina precisa de teste e ajuste.',
'Mas atenção: visualização não é venda. Para vender, você precisa de uma oferta que faça sentido para quem acompanha sua página.',
'Quer conhecer o FP e entender como começar com páginas sem aparecer? Comente FP. Eu te mostro os detalhes.'
]
async def scene(i,text):
 words=[]
 with open(ROOT/f'public/voice-{i}.mp3','wb') as f:
  async for chunk in edge_tts.Communicate(text,'pt-BR-AntonioNeural',rate='+8%',boundary='WordBoundary').stream():
   if chunk['type']=='audio': f.write(chunk['data'])
   elif chunk['type']=='WordBoundary':
    start=chunk['offset']/10000; end=(chunk['offset']+chunk['duration'])/10000
    words.append(dict(text=chunk['text'],startMs=start,endMs=end,timestampMs=start,confidence=None))
 dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(ROOT/f'public/voice-{i}.mp3')]))
 return dict(text=text,frames=math.ceil((dur+0.45)*30),captions=words)
async def main():
 data=await asyncio.gather(*(scene(i,t) for i,t in enumerate(SCRIPTS)))
 (ROOT/'src/timing.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print([(x['frames'],len(x['captions'])) for x in data]); print('total',sum(x['frames'] for x in data)/30)
asyncio.run(main())
