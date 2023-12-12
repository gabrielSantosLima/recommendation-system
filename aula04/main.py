from math import sqrt

import streamlit as st

musics = {"Dr Dog/Fate": {"piano": 2.5, "vocals": 4, "beat": 3.5, "blues": 3, "guitar": 5, "backup vocals": 4, "rap": 1},
         "Phoenix/Lisztomania": {"piano": 2, "vocals": 5, "beat": 5, "blues": 3, "guitar": 2, "backup vocals": 1, "rap": 1},
         "Heartless Bastards/Out at Sea": {"piano": 1, "vocals": 5, "beat": 4, "blues": 2, "guitar": 4, "backup vocals": 1, "rap": 1},
         "Todd Snider/Don't Tempt Me": {"piano": 4, "vocals": 5, "beat": 4, "blues": 4, "guitar": 1, "backup vocals": 5, "rap": 1},
         "The Black Keys/Magic Potion": {"piano": 1, "vocals": 4, "beat": 5, "blues": 3.5, "guitar": 5, "backup vocals": 1, "rap": 1},
         "Glee Cast/Jessie's Girl": {"piano": 1, "vocals": 5, "beat": 3.5, "blues": 3, "guitar":4, "backup vocals": 5, "rap": 1},
         "La Roux/Bulletproof": {"piano": 5, "vocals": 5, "beat": 4, "blues": 2, "guitar": 1, "backup vocals": 1, "rap": 1},
         "Mike Posner/Testing": {"piano": 2.5, "vocals": 4, "beat": 4, "blues": 1, "guitar": 1, "backup vocals": 1, "rap": 1},
         "Black Eyed Peas/Rock That Body": {"piano": 2, "vocals": 5, "beat": 5, "blues": 1, "guitar": 2, "backup vocals": 2, "rap": 4},
         "Lady Gaga/Alejandro": {"piano": 1, "vocals": 5, "beat": 3, "blues": 2, "guitar": 1, "backup vocals": 2, "rap": 1}}


# Função para calcular a distância de Manhattan
def manhattan(music1, music2):
    distance = 0
    total = 0
    for key in music1:
        if key in music2:
            distance += abs(music1[key] - music2[key])
            total += 1
    return distance

# Função para recomendar música com base nas preferências do usuário
def recommend(music_name, musics):
    userProfile = musics[music_name]
    distances = []
    for music in musics:
        if music != music_name:  # Não queremos comparar com a própria música
            distance = manhattan(musics[music], userProfile)
            distances.append((distance, music, musics[music]))
    distances.sort()  # Ordena com base na distância (mais próximo primeiro)
    return distances

# Função para adicionar uma nova música à playlist
def adicionar_musica_playlist(playlist, nome_musica, userProfile):
    playlist[nome_musica] = userProfile

# Streamlit frontend
st.title("Playlist Inteligente")


# Sidebar para escolher a música a ser adicionada à playlist
st.sidebar.title("Escolha seu perfil de música")
# selected_music = st.sidebar.selectbox("Selecione uma música:", list(musics.keys()))
piano = st.sidebar.slider('piano', max_value=5)
vocals = st.sidebar.slider('vocals', max_value=5) 
beat = st.sidebar.slider('beat', max_value=5) 
blues = st.sidebar.slider('blues', max_value=5) 
guitar = st.sidebar.slider('guitar', max_value=5) 
bv = st.sidebar.slider('bv', max_value=5) 
rap = st.sidebar.slider('rap', max_value=5) 
# Playlist inicial
playlist = {}

explanation = None

# Adiciona a música escolhida à playlist
if st.sidebar.button("Recomendar músicas"):
    st.sidebar.success(f"Meu perfil adicionado")
    
    profile_music = {
        "Meu perfil": {
            "piano": piano, 
            "vocals": vocals, 
            "beat": beat, 
            "blues": blues, 
            "guitar": guitar, 
            "backup vocals": bv, 
            "rap": rap
        }
    }
    adicionar_musica_playlist(playlist, "Meu perfil", profile_music)
    adicionar_musica_playlist(musics, "Meu perfil", profile_music["Meu perfil"])

def menor_distancia(musica1, perfil) -> str:
    last = (musica1['piano'], 'piano')
    last_last = (musica1['vocals'], 'vocals')

    for field, item in musica1.items():
        carac1 = item
        carac2 = perfil[field]  
        distance = abs(carac1 - carac2)

        if distance < last[0]:
            last = (distance, field)
        elif distance < last_last[0] and last[1] != field:
            last_last = (distance, field)

    return last[1], last_last[1]

# Atualiza a playlist com músicas similares à última adicionada
if playlist:
    st.subheader("Sua Playlist:")
    st.write(list(playlist.keys()))



    # Obtém recomendações para a última música adicionada à playlist
    ultima_musica_adicionada = list(playlist.keys())[-1]
    recomendacoes = recommend(ultima_musica_adicionada, musics)

    st.subheader("Músicas Baseadas na Última Música Adicionada:")

    for distancia, musica, musica_el in recomendacoes:
        carac1, carac2 = menor_distancia(musica_el, musics[ultima_musica_adicionada])
        st.write(f"{musica} - Distância: {distancia}. Recomendando pelas características '{carac1}' e '{carac2}' pois são semelhantes")
        