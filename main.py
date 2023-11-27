'''
Baixando um vídeo privado do Vimeo que está incorporado a uma página da web, usando a biblioteca "vimeo-downloader":
'''
# https://pypi.org/project/vimeo-downloader/#description

# https://arnavbonigala.medium.com/download-any-video-from-the-web-bfc3931f0950


from vimeo_downloader import Vimeo

# Crie uma instância do Vimeo com a URL do vídeo e a URL onde ele está incorporado
link_videos = Vimeo('https://vimeo.com/869627766', embedded_on='https://on.fiap.com.br/local/salavirtual/conteudo-video.php?c=9959&id=356473')

# Obtenha os streams disponíveis para o vídeo
quality_video = link_videos.streams

print(quality_video)
# Selecione o melhor stream (geralmente o último na lista)
best_stream = quality_video[-1]

# Baixe o vídeo
best_stream.download(download_directory='DirectoryName', filename='Dando_nome_ao_vídeo_2')


'''
Obs: substitua 'URL_DA_PÁGINA_ONDE_O_VÍDEO_ESTÁ_INCORPORADO' pela URL real da página onde o vídeo está incorporado.

Lembre-se de que baixar vídeos privados pode violar os termos de serviço do Vimeo, então certifique-se de ter permissão para fazer isso. Além disso, esteja ciente de que este método pode não funcionar para todos os vídeos privados, pois alguns podem ter proteções adicionais implementadas. Além disso, você precisa ter cuidado ao lidar com dados sensíveis, como suas credenciais de login. Não compartilhe suas credenciais de login ou outras informações sensíveis publicamente. Se você estiver em um ambiente compartilhado, certifique-se de que suas informações estão seguras.
'''