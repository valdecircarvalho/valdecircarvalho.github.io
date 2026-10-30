# Implementação da auditoria — 30/10/2026

Escopo: VCARVALHO-4. Alterações para revisão em PR; sem merge ou publicação direta.

## Decisões e entrega

- Manter os canonicals existentes em `/index.html` e `/index-ptbr.html`; sitemap somente com essas duas URLs, alternates recíprocos EN/PT-BR/x-default.
- `lastmod` registra 30/10/2026, data desta revisão substancial. Não atualizar automaticamente em builds.
- Páginas de erro com `noindex, follow`, sem alternates para homes. Nenhuma regra de redirecionamento ou fallback HTTP foi adicionada.
- `ProfilePage` identifica cada tradução; `mainEntity` usa a mesma `Person` com `https://valdecir.com/#person`. Removidos fatos estruturados sem correspondência visível (formação, idiomas, nacionalidade e lista adicional de habilidades).
- Síntese profissional, perguntas úteis e links textuais de contato em ambos os idiomas. Preservados cargo na Vertigo, interesses e personalidade.
- Retirado o bloco de credenciais sem comprovação, em ambas as versões. Não se presume que as alegações sejam falsas; faltam contexto e evidência publicáveis. Nenhum número substituto foi criado.
- Não criadas páginas de casos ou palestra incompletas. A dependência editorial é parte pendente do escopo, permitida pelos critérios da issue.
- Mantido o bloqueio genérico de PDFs: não há confirmação editorial de quais materiais devem ser descobertos. O nome do arquivo não comprova data de apresentação, autoria, evento ou permissão.

## Insumos necessários para concluir conteúdo e autoridade

| Item | Informação necessária |
| --- | --- |
| Crescimento de 105% da comunidade C2C | Datas inicial/final, definição de membros/atividade, valores de base e final, papel pessoal e registro público verificável autorizado. |
| Seis capítulos VMUG | Quais capítulos, cidades, datas de fundação, papel individual versus equipe e links oficiais/históricos. |
| Mais de 50 clientes Oracle OCVS | Período, definição e contagem de clientes, contribuição individual, fonte pública e autorização de divulgação sem expor clientes. |
| VMware vExpert, Veeam Vanguard e HashiCorp Ambassador | Perfil/lista oficial identificando Valdecir, anos reconhecidos e distinção entre reconhecimento histórico e vigente. |
| Caso 1 e caso 2 (cada um) | Projeto/contexto autorizado; problema; período; papel pessoal; restrições; decisões e abordagem; resultados observados e método de medição; links/evidências; limitações; autoria e revisão PT/EN. Casos podem omitir nomes e números, mas precisam de relato original validado. |
| Palestra/material | Título, autoria, data e evento confirmados; resumo e tópicos revisados; URL pública de evento/vídeo/deck; autorização de divulgação e tradução. Candidato existente: `assets/files/share/2025-07-14-deck-rpa-expo-tqi.pdf`; o nome não foi tratado como comprovação. |

Quando validados: publicar HTML PT/EN equivalente, ligar pelas homes, acrescentar somente URLs canônicas ao sitemap com datas reais e abrir exceção em robots somente para PDF explicitamente aprovado. Robots não protege material privado.

## Acompanhamento após publicação

Responsável pelo site: confirmar implantação via fluxo do repositório; conferir HTTP 200 nas homes, XML/robots acessíveis e 404 em caminho inexistente. Verificar `noindex` nas páginas auxiliares e markup no Schema Validator. Enviar sitemap no Search Console somente com acesso autorizado.

Sem acesso a Search Console ou analytics nesta execução: nenhuma linha de base privada estabelecida. Registrar data de publicação e exportar, quando disponível, indexação por URL, consultas, impressões, cliques e CTR; comparar janelas consecutivas de 28 dias, separando marca, temas e idiomas. Registrar contatos com origem declarada/medida, sem presumir que cliques em e-mail equivalem a conversões e sem coletar mensagens pessoais nos relatórios. Não instalar rastreamento sem definição do proprietário.

Mensalmente repetir amostra fixa em sistemas de IA:
1. Quem é Valdecir Carvalho?
2. Em que temas de inteligência artificial Valdecir Carvalho trabalha?
3. Como entrar em contato com Valdecir Carvalho?
4. Que materiais públicos de Valdecir Carvalho tratam de modernização de aplicações?
5. What does Valdecir Carvalho work on?

Guardar ferramenta/modelo, data, pergunta exata, resposta, URLs citadas e contexto de sessão; distinguir citação, clique e contato. Não interpretar a amostra como ranking universal. Não há promessa de rankings, citações, resultados enriquecidos ou benefício de `llms.txt`; não adicionado FAQ schema.

## Referências técnicas

- [ProfilePage — Schema.org](https://schema.org/ProfilePage)
- [Versões localizadas — Google](https://developers.google.com/search/docs/specialty/international/localized-versions)

## Verificação reproduzível

`python3 -m unittest discover -s tests -v`: sitemap/canonicals/alternates, noindex, identidade estruturada, logo PT e existência dos links/arquivos internos. A suíte inicialmente detectou os defeitos e passou após os ajustes. Não valida entrega HTTP do provedor nem elegibilidade de resultados enriquecidos.

## Evidências desta execução

- Cinco testes passaram; `git diff --check` sem erros. Revisão independente apontou contraste dos contatos na seção verde; corrigido com texto preto nessa seção e branco nas seções escuras.
- HTTP público em 30/10/2026: homes, páginas auxiliares, sitemap, robots e deck existente responderam 200; `/seo-validation-vcarvalho-4-missing` respondeu 404. São verificações do site vigente, anteriores ao merge deste PR. Confirmar os novos metadados após implantação.
- Chromium/Playwright: PT e EN a 390×900 e 1440×900, sem overflow horizontal e sem imagens quebradas. Capturas completas usam animações AOS desativadas apenas na captura para revelar as seções fora do viewport. CSS/JS de produção continuam com o comportamento anterior.
- Lighthouse 13.6.0, mobile, servidor HTTP local, CPU 4×, RTT 150 ms e throughput 1638,4 Kbps; uma execução por revisão, mesma máquina. Referência: commit `d36e3b6`. Medições finais usam fontes disponíveis no ambiente; primeiras tentativas sem bibliotecas/fontes do navegador foram descartadas.

| Métrica | Referência | Alteração |
| --- | --- | --- |
| Performance | 61 | 69 |
| Acessibilidade automática | 93 | 93 |
| SEO automático | 100 | 100 |
| First Contentful Paint | 3,5 s | 3,5 s |
| Largest Contentful Paint | 4,7 s | 3,5 s |
| Total Blocking Time | 0 ms | 0 ms |
| Cumulative Layout Shift | 0,290 | 0,285 |
| Speed Index | 3,5 s | 3,5 s |

A amostra local não demonstra ganho de produção nem substitui dados de campo. CLS permanece elevado; os escores não certificam acessibilidade ou indexação. Não reduzidas fontes/dependências: uma rodada não isola gargalos e o escopo editorial não exige essa alteração. Próxima investigação de desempenho: repetir séries de medições no site implantado, localizar deslocamentos de layout e avaliar fontes/dependências com comparação visual antes de removê-las.
