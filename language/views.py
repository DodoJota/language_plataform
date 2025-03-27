
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .models import Material, Contato, Video, Teacher, Student

from django.shortcuts import get_object_or_404


@login_required
def portugues(request):
    return render(request, "portugues.html")

def teacher(request):
    context = {
        'total_aulas': Video.objects.count(),
        'aulas_video': Video.objects.filter(arquivo='video').count(),
        'total_materiais': Material.objects.count(),
        'materiais_pdf': Material.objects.filter(tipo='PDF').count(),  # Alterado para usar o campo 'tipo'
        'materiais_outros': Material.objects.exclude(tipo='PDF').count(),  # Conta tudo que não é PDF
    }
    return render(request, 'teacher.html', context)

@login_required
def students_dashboard(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
        alunos = teacher.students.all().select_related('user')
    except Teacher.DoesNotExist:
        return redirect('login')

    context = {
        'alunos': alunos,
        'total_alunos': alunos.count(),
    }
    return render(request, 'students.html', context)

def aulas(request):
    videos = Video.objects.all().order_by('modulo', 'ordem')
    videos_por_modulo = {}

    for video in videos:
        if video.modulo not in videos_por_modulo:
            videos_por_modulo[video.modulo] = []
        videos_por_modulo[video.modulo].append(video)
    
    return render(request, 'aulas.html', {'videos_por_modulo': videos_por_modulo})

def praticar(request):
    return render(request, 'praticar.html')

def students(request):
    return render(request, 'students.html')

def landing(request):
    return render(request, 'landing.html')

def flashcards(request):
    return render(request, 'flashcards.html')

def faces(request):
    return render(request, 'faces.html')

def gramatica(request):
    return render(request, 'gramatica.html')

def materiais(request):
    materiais = Material.objects.all().order_by('-data_envio')
    return render(request, 'materiais.html', {'materiais': materiais})

def dicionario(request):
    return render(request, 'dicionario.html')

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        print(request.POST) 

        Contato.objects.create(nome=nome, email=email, mensagem=mensagem)

        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('contato') 

    return render(request, 'contato.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Verifica se o usuário é o professor
            if user.username == 'professor':  # Identifica o professor pelo nome de usuário
                return redirect('teacher')  # Redireciona para a página do professor
            else:
                return redirect('portugues')  # Redireciona para a página do estudante
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("/login/")


def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Verifica se todos os campos foram preenchidos
        if not username or not email or not password or not confirm_password:
            messages.error(request, 'Todos os campos são obrigatórios!')
            return render(request, 'create_user.html')

        # Verifica se as senhas coincidem
        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'create_user.html')

        # Verifica se o username já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já está em uso!')
            return render(request, 'create_user.html')

        # Verifica se o email já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Já existe uma conta com este email!')
            return render(request, 'create_user.html')

        try:
            # Cria o usuário
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            messages.success(request, 'Usuário criado com sucesso! Faça login para continuar.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Erro ao criar o usuário: {e}')

    return render(request, 'create_user.html')

def enviar_materiais(request):
    if request.method == 'POST':
        if 'material' in request.FILES:
            uploaded_file = request.FILES['material']
            tipo = request.POST.get('tipo', 'PDF')
            
            # Validação simples para PDF
            if tipo == 'PDF' and not uploaded_file.name.lower().endswith('.pdf'):
                messages.error(request, 'Por favor, envie um arquivo com extensão .pdf para materiais PDF')
                return redirect('enviar_materiais')
            
            Material.objects.create(
                nome=uploaded_file.name,
                arquivo=uploaded_file,
                tipo=tipo
            )
            messages.success(request, 'Material enviado com sucesso!')
            return redirect('enviar_materiais')
    
    # Filtragem
    materiais = Material.objects.all().order_by('-data_envio')
    tipo_filtro = request.GET.get('tipo_filtro')
    if tipo_filtro:
        materiais = materiais.filter(tipo=tipo_filtro)
    
    return render(request, 'enviar_materiais.html', {'materiais': materiais})

def deletar_material(request, material_id):
    # Obtém o material pelo ID ou retorna 404 se não existir
    material = get_object_or_404(Material, id=material_id)
    
    # Remove o arquivo do sistema de arquivos
    if material.arquivo:  # Verifica se o arquivo existe
        fs = FileSystemStorage()
        fs.delete(material.arquivo.path)  # Usa .path para obter o caminho do arquivo
    
    # Remove o material do banco de dados
    material.delete()
    
    # Redireciona para a página de materiais
    return redirect('enviar_materiais')

def enviar_videos(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        modulo = request.POST.get('modulo')
        ordem = request.POST.get('ordem')
        arquivo = request.FILES.get('video')

        if titulo and modulo and ordem and arquivo:
            Video.objects.create(titulo=titulo, modulo=modulo, ordem=ordem, arquivo=arquivo)
            messages.success(request, 'Vídeo enviado com sucesso!')
            return redirect('enviar_videos')
        else:
            messages.error(request, 'Preencha todos os campos e selecione um vídeo.')
            return redirect('enviar_videos')
    
    videos = Video.objects.all().order_by('modulo', 'ordem')
    return render(request, 'enviar_videos.html', {'videos': videos})

def deletar_video(request, video_id):
    # Busca o vídeo pelo ID ou retorna um erro 404 se não existir
    video = get_object_or_404(Video, id=video_id)
    
    try:
        # Exclui o vídeo
        video.delete()
        messages.success(request, 'Vídeo excluído com sucesso!')
    except Exception as e:
        # Em caso de erro, exibe uma mensagem de erro
        messages.error(request, f'Ocorreu um erro ao excluir o vídeo: {str(e)}')
    
    # Redireciona de volta para a página de envio de vídeos
    return redirect('enviar_videos')


##############################################################

# PENSAR EM INTEGRAÇÃO MARCACAO DE AULA COM GOOGLE CALENDAR DO TUTOR VIA API GOOGLE
# OFERECER PACOTES COMO NO HIWELL