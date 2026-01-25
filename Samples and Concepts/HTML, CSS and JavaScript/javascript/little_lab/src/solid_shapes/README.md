# SOLID com Formas (incremental)

Este diretório mostra um exemplo propositalmente ruim e uma sequência de refactors incrementais até ficar **compliance com SOLID**, usando o cenário de **formas geométricas** (inspirado em `src/shape.js`).

## Como rodar

No diretório `little_lab`:

```bash
node src/solid_shapes/00-violates-all.js
node src/solid_shapes/01-srp.js
node src/solid_shapes/02-ocp.js
node src/solid_shapes/03-lsp.js
node src/solid_shapes/04-isp.js
node src/solid_shapes/05-dip.js
node src/solid_shapes/06-solid.js
```

## Etapas

- **00-violates-all.js**: um “anti-exemplo” que viola SRP/OCP/LSP/ISP/DIP ao mesmo tempo.
- **01-srp.js**: separa responsabilidades (modelos vs geração/ordenação vs I/O vs apresentação).
- **02-ocp.js**: remove `if/switch` por tipo e usa registro/factory extensível (adiciona shapes sem modificar o core).
- **03-lsp.js**: evita herança que quebra contrato (Square não é Rectangle).
- **04-isp.js**: separa as necessidades do cliente em capabilities pequenas (HasArea / HasPerimeter / HasCircumference).
- **05-dip.js**: injeta dependências (rng/logger/repo) e remove acoplamento direto com infra no alto nível.
- **06-solid.js**: versão final unificando as ideias e ficando alinhada com SOLID.
