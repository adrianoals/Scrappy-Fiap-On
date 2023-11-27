from vimeo_downloader import Vimeo


lista_vimeo = ["https://vimeo.com/209756871", "https://vimeo.com/209804720", "https://vimeo.com/210603780", "https://vimeo.com/210596488", "https://vimeo.com/210605843", "https://vimeo.com/210658009", "https://vimeo.com/210609856"]

nome_videos =["1 - Estratégia", "2 - Processo de Planejamento", "3 - Análise SWOT", "4 - Matriz BCG", "5 - BSC: Balanced Scorecard", "6 - Mapas Estratégicos", "7 - Alinhamento Estratégico"]

url = 'https://on.fiap.com.br/local/salavirtual/conteudo-video.php?c=9053&id=318417'


for vimeo_link, nome_video in zip(lista_vimeo, nome_videos):
    # Crie uma instância do Vimeo com a URL do vídeo e a URL onde ele está incorporado
    link_videos = Vimeo(vimeo_link, embedded_on=url)
    # Obtenha os streams disponíveis para o vídeo
    quality_video = link_videos.streams
    print(quality_video)

    # Selecione o melhor stream (geralmente o último na lista)
    best_stream = quality_video[-3]

    # Baixe o vídeo
    best_stream.download(download_directory='DirectoryName', filename=nome_video)

