# FP — Neon

Vídeo vertical original para o treinamento FP, inspirado na linguagem visual da referência fornecida: fundo escuro, rosa neon, celulares e painéis animados. 1080 × 1920, 30 fps, 51,93 segundos.

## Usar

```sh
npm install
python3 generate_music.py
npm run studio
npm run render
```

O GitHub Actions `Render FP Neon` também gera o MP4 e seis quadros de conferência. Baixe o artefato `FP-Neon-video` na execução concluída.

A narração e os tempos por palavra estão incluídos. A música foi sintetizada para este projeto. Os gráficos são ilustrações; não representam resultados reais. CTA: “Comente FP”.

As cenas ficam em `src/`; cada uma tem composição independente. `timing.json` guarda o texto, duração e tempos das palavras. `generate_audio.py` recria as vozes com edge-tts; ao alterar texto, ajuste também as durações em `Main.tsx` e `index.tsx`.

Este projeto está em uma branch própria. Não faça merge da branch para publicar um site; os arquivos de vídeo não exigem alterações no site.
